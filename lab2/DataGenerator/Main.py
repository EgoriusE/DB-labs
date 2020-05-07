import click
from Adder import *
from Utils import *
from Deleter import *

@click.group()
def cli():
    pass


@click.command()
@click.option('-table', default="group", help='Name of the table')
@click.option('-n', default=10_000, help='The number of records')
def add(table, n):
    if table == "user":
        add_users(n)
    elif table == "group":
        add_groups(n)
    elif table == "artist":
        add_artists(n)
    elif table == "album":
        add_albums(n)
    elif table == "song":
        add_songs(n)
    elif table == "playlist":
        add_playlists(n)
    elif table == "songs_area":
        add_songs_area(n)
    elif table == "groups_area":
        add_groups_area(n)
    elif table == "users_area":
        add_users_area(n)
    elif table == "all":
        add_all(n)


@click.command()
@click.option('-table', default="group", help='Delete all records in table')
def delete(table):
    cursor, conn = open_connection()
    if table == "album":
        cursor.execute('delete from album;')
    elif table == "artist":
        cursor.execute('delete from artist;')
    elif table == "user":
        cursor.execute('delete from "user";')
    elif table == "group":
        cursor.execute('delete from "group";')
    elif table == "song":
        cursor.execute('delete from song;')
    elif table == "playlist":
        cursor.execute('delete from playlist;')
    elif table == "playlists_table":
        cursor.execute('delete from playlists_table;')
    elif table == "songs_area":
        delete_songs_area(cursor)
    elif table == "groups_area":
        delete_groups_area(cursor)
    elif table == "users_area":
        delete_users_area(cursor)
    elif table == "all":
        delete_users_area(cursor)
        delete_groups_area(cursor)
        delete_songs_area(cursor)

    cursor.execute("commit;")
    print("All records were deleted in ", table)
    close_connection(cursor, conn)


cli.add_command(delete)
cli.add_command(add)

if __name__ == '__main__':
    cli()
