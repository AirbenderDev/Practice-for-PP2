from config import LIMIT, OFFSET
from connect import get_conn


def create_table():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE,
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()


def add_or_update():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def search():
    p = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (p,))
    print(cur.fetchall())
    cur.close()
    conn.close()


def add():
    name = input()
    phone = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


def add_many():
    names = input().split()
    phones = input().split()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL insert_many(%s, %s)", (names, phones))
    conn.commit()
    cur.close()
    conn.close()


def get_page():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)",
                (LIMIT, OFFSET))
    print(cur.fetchall())
    cur.close()
    conn.close()


def delete():
    p = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s)", (p,))
    conn.commit()
    cur.close()
    conn.close()


def search():
    pattern = input("Search: ")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete():
    name = input("Delete name: ")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (name,))

    conn.commit()
    cur.close()
    conn.close()


def menu():
    create_table()

    while True:
        print("\n1. Add/Update")
        print("2. Search")
        print("3. Delete")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_or_update()
        elif choice == "2":
            search()
        elif choice == "3":
            delete()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
