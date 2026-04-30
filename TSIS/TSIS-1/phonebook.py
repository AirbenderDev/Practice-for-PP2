import csv
import json
from connect import get_conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    for f in ["schema.sql", "procedures.sql"]:
        cur.execute(open(f).read())
    conn.commit()
    cur.close()
    conn.close()


def print_row(r):
    print(f"  [{r[0]}] {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")


def add_contact():
    name = input("Name: ")
    email = input("Email: ") or None
    bday = input("Birthday (YYYY-MM-DD): ") or None
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ") or "mobile"
    group = input("Group (Family/Work/Friend/Other): ") or "Other"

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    row = cur.fetchone()
    if row:
        gid = row[0]
    else:
        cur.execute(
            "INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
        gid = cur.fetchone()[0]
    cur.execute("INSERT INTO contacts(name,email,birthday,group_id) VALUES(%s,%s,%s,%s) RETURNING id",
                (name, email, bday, gid))
    cid = cur.fetchone()[0]
    cur.execute(
        "INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)", (cid, phone, ptype))
    conn.commit()
    cur.close()
    conn.close()
    print("Added!")


def show_all():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM contacts")
    total = cur.fetchone()[0]
    offset = 0
    while True:
        cur.execute("SELECT * FROM get_contacts_page(5, %s)", (offset,))
        rows = cur.fetchall()
        print(f"\n--- page {offset//5+1} ---")
        for r in rows:
            print_row(r)
        cmd = input("[n]ext [p]rev [q]uit: ").strip()
        if cmd == "n" and offset+5 < total:
            offset += 5
        elif cmd == "p" and offset > 0:
            offset -= 5
        elif cmd == "q":
            break
    cur.close()
    conn.close()


def search():
    q = input("Query: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    rows = cur.fetchall()
    if not rows:
        print("Nothing found.")
    for r in rows:
        print_row(r)
    cur.close()
    conn.close()


def filter_group():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id,name FROM groups")
    for g in cur.fetchall():
        print(f"  {g[0]}. {g[1]}")
    gid = input("Group id: ")
    cur.execute("""
        SELECT c.id,c.name,c.email,c.birthday,g.name,
               STRING_AGG(p.phone||' ('||COALESCE(p.type,'?')||')',', ')
        FROM contacts c
        LEFT JOIN groups g ON g.id=c.group_id
        LEFT JOIN phones p ON p.contact_id=c.id
        WHERE c.group_id=%s GROUP BY c.id,c.name,c.email,c.birthday,g.name
    """, (gid,))
    for r in cur.fetchall():
        print_row(r)
    cur.close()
    conn.close()


def add_phone():
    name = input("Contact name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ") or "mobile"
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()
    cur.close()
    conn.close()
    print("Done!")


def move_group():
    name = input("Contact name: ")
    group = input("New group: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL move_to_group(%s,%s)", (name, group))
    conn.commit()
    cur.close()
    conn.close()
    print("Done!")


def delete_contact():
    name = input("Name to delete: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted.")


def export_json():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id,c.name,c.email,c.birthday::text,g.name,
               JSON_AGG(JSON_BUILD_OBJECT('phone',p.phone,'type',p.type)) FILTER(WHERE p.id IS NOT NULL)
        FROM contacts c
        LEFT JOIN groups g ON g.id=c.group_id
        LEFT JOIN phones p ON p.contact_id=c.id
        GROUP BY c.id,c.name,c.email,c.birthday,g.name
    """)
    data = [{"id": r[0], "name": r[1], "email": r[2], "birthday": r[3],
             "group": r[4], "phones": r[5] or []} for r in cur.fetchall()]
    json.dump(data, open("contacts.json", "w"), indent=2)
    print(f"Exported {len(data)} contacts.")
    cur.close()
    conn.close()


def import_json():
    data = json.load(open(input("JSON file: ") or "contacts.json"))
    conn = get_conn()
    cur = conn.cursor()
    for c in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (c["name"],))
        if cur.fetchone():
            if input(f"'{c['name']}' exists. [s]kip/[o]verwrite? ") != "o":
                continue
            cur.execute("DELETE FROM contacts WHERE name=%s", (c["name"],))
        group = c.get("group", "Other")
        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        row = cur.fetchone()
        if row:
            gid = row[0]
        else:
            cur.execute(
                "INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
            gid = cur.fetchone()[0]
        cur.execute("INSERT INTO contacts(name,email,birthday,group_id) VALUES(%s,%s,%s,%s) RETURNING id",
                    (c.get("name"), c.get("email"), c.get("birthday"), gid))
        cid = cur.fetchone()[0]
        for ph in (c.get("phones") or []):
            cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)",
                        (cid, ph.get("phone"), ph.get("type")))
    conn.commit()
    cur.close()
    conn.close()
    print("Imported!")


def import_csv():
    conn = get_conn()
    cur = conn.cursor()
    for row in csv.DictReader(open(input("CSV file: ") or "contacts.csv")):
        name, phone = row.get("name", "").strip(), row.get("phone", "").strip()
        if not name or not phone:
            continue
        group = row.get("group", "Other").strip()
        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        gr = cur.fetchone()
        if gr:
            gid = gr[0]
        else:
            cur.execute(
                "INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
            gid = cur.fetchone()[0]
        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        ex = cur.fetchone()
        if not ex:
            cur.execute("INSERT INTO contacts(name,email,birthday,group_id) VALUES(%s,%s,%s,%s) RETURNING id",
                        (name, row.get("email") or None, row.get("birthday") or None, gid))
            cid = cur.fetchone()[0]
        else:
            cid = ex[0]
        cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)",
                    (cid, phone, row.get("type", "mobile")))
    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported!")


MENU = """
1. Add contact    6. Add phone
2. Show all       7. Move to group
3. Search         8. Delete
4. Filter group   9. Export JSON
5. Import JSON   10. Import CSV
0. Exit
"""


def main():
    init_db()
    actions = {
        "1": add_contact, "2": show_all,   "3": search,
        "4": filter_group, "5": import_json, "6": add_phone,
        "7": move_group,  "8": delete_contact, "9": export_json, "10": import_csv
    }
    while True:
        print(MENU)
        c = input("Choice: ").strip()
        if c == "0":
            break
        elif c in actions:
            try:
                actions[c]()
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
