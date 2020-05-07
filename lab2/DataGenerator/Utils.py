import psycopg2


def open_connection():
    conn = psycopg2.connect(dbname='EgMusic', user='postgres',
                            password='9368', host='localhost')
    cursor = conn.cursor()
    return cursor, conn


def close_connection(cursor, conn):
    cursor.execute('commit;')
    cursor.close()
    conn.close()



