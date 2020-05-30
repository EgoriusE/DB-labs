import psycopg2


def open_connection():
    conn = psycopg2.connect(dbname='EgMusic', user='postgres',
                            password='9368', host='localhost')
    cursor = conn.cursor()
    conn.autocommit = True

    return conn, cursor


def close_connection(cursor, conn):
    cursor.execute('commit;')
    cursor.close()
    conn.close()


def drop_index():
    conn, cursor = open_connection()
    cursor.execute("DROP INDEX IF EXISTS us_ind_1")
    cursor.execute("DROP INDEX IF EXISTS us_ind_2")
    cursor.execute("DROP INDEX IF EXISTS us_ind_3")
    cursor.execute("DROP INDEX IF EXISTS pl_id")
    cursor.execute("DROP INDEX IF EXISTS album_type_ind")
    cursor.execute("DROP INDEX IF EXISTS song_id_ind")
    cursor.execute("DROP INDEX IF EXISTS user_email_ind")
    cursor.execute("DROP INDEX IF EXISTS artists_id")
    close_connection(cursor, conn)

