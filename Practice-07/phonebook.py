import csv
from connect import get_connection


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def update_contact():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE name=%s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()


def delete_contact():
    name = input("Enter name to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()


def search_contacts():
    keyword = input("Search (name): ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name = %s",
        (keyword, )
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def import_csv():
    file_name = input("Enter CSV file name: ")

    conn = get_connection()
    cur = conn.cursor()

    with open(file_name, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            name, phone = row
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("PHONEBOOK MENU")
        print("1. Add contact")
        print("2. Show contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Search contact")
        print("6. Import CSV")
        print("0. Exit")

        choice = int(input("Choose: "))
        match choice:
            case 1:
                add_contact()
            case 2:
                show_contacts()
            case 3:
                update_contact()
            case 4:
                delete_contact()
            case 5:
                search_contacts()
            case 6:
                import_csv()
            case 0:
                print("Bye!")
                break
            case _:
                continue


if __name__ == "__main__":
    menu()
