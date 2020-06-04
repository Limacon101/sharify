import psycopg2
from etl_sql_queries import create_table_queries, drop_table_queries
import connect
import os
from dotenv import load_dotenv

load_dotenv()
HOSTNAME = os.getenv('DB_HOSTNAME')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
DEFAULT_DBNAME = os.getenv('DB_DEFAULT_NAME')

# Working DB:
DBNAME = os.getenv('DB_NAME')


def create_db():
    connect.reset_db()

    return connect.connect()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


if __name__ == '__main__':
    try:
        cur, conn = create_db()
        drop_tables(cur, conn)
        create_tables(cur, conn)
    finally:
        conn.close()
