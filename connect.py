import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'sharify'
PASSWORD = 'sharify'
DEFAULT_DBNAME = 'sharify'

DBNAME = 'sharifydb'


def reset_db():
    # Uses default db to recreate a new one
    conn = psycopg2.connect("host={} dbname={} user={} password={}"
                            .format(HOSTNAME, DEFAULT_DBNAME, USERNAME, PASSWORD))
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute('DROP DATABASE IF EXISTS {}'.format(DBNAME))
    cur.execute('CREATE DATABASE {} WITH ENCODING "utf8" TEMPLATE template0'.format(DBNAME))

    conn.close()


def connect(autocommit=True):
    # todo: refactor to a context manager
    conn = psycopg2.connect("host={} dbname={} user={} password={}"
                            .format(HOSTNAME, DBNAME, USERNAME, PASSWORD))
    conn.set_session(autocommit=autocommit)
    cur = conn.cursor()

    return cur, conn