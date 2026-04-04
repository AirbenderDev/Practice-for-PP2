from connect import get_conn
from config import LIMIT, OFFSET


def add():
    name = input("name: ")
    phone = input("phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL insert_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


def update():
    name = input("name: ")
    phone = input("phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


def delete():
    p = input("name or phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s)", (p,))
    conn.commit()
    cur.close()
    conn.close()


def search():
    p = input("search: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (p,))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1 add")
        print("2 update")
        print("3 delete")
        print("4 search")
        print("0 exit")
        c = input(">> ")
        if c == "1":
            add()
        elif c == "2":
            update()
        elif c == "3":
            delete()
        elif c == "4":
            search()
        elif c == "0":
            break


if __name__ == "__main__":
    menu()
