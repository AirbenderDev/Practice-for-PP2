import psycopg2


def get_conn():
    return psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="altai",
        password="altai"
    )
