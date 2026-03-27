import psycopg2
from config import connection_for_DB


def get_connection():
    return psycopg2.connect(**connection_for_DB)
