from ArtistGenerator import ArtistGenerator
from AlbumGenerator import AlbumGenerator
from SongGenerator import SongGenerator
from PlaylistGenerator import PlaylistGenerator
from UserGenerator import UserGenerator
from GroupGenerator import GroupGenerator
from Utils import close_connection, open_connection
import random


def add_playlists(n):
    cursor, conn = open_connection()
    gen_playlist = PlaylistGenerator()
    data = gen_playlist.get_primary_key_data(n)
    for d in data:
        params = gen_playlist.get_params()
        print('id: ', d, params, sep=': ')
        cursor.execute(
            'insert into playlist (id, name, quantity, author, duration, icon_path) VALUES (%s, %s, %s, %s, %s, '
            '%s);commit;',
            (d, params.get('name'), params.get('quantity'), params.get('author'), params.get('duration'),
             params.get('icon_path')))
    print(n, "Playlists added", sep=' ')
    close_connection(cursor, conn)


def add_songs(n):
    cursor, conn = open_connection()
    song_generator = SongGenerator()
    data = song_generator.get_primary_key_data(n)
    for s in data:
        params = song_generator.get_params()
        print('id: ', s, params, sep=': ')
        cursor.execute('insert into song (id, name, path, album) values (%s, %s, %s, %s);commit;',
                       (s, params.get('name'), params.get('path'), params.get('album')))
    print(n, "Songs added", sep=' ')
    close_connection(cursor, conn)


def add_albums(n):
    cursor, conn = open_connection()

    gen_albums = AlbumGenerator()
    data = gen_albums.get_primary_key_data(n)
    for d in data:
        params = gen_albums.get_params()
        print('id: ', d, params, sep=': ')
        cursor.execute(
            'insert into album (id, name, year, duration, quantity, icon_path) values (%s, %s, %s, %s, %s, '
            '%s);commit;',
            (d, params.get('name'), params.get('year'), params.get('duration'), params.get('quantity'),
             params.get('icon_path')))
    print(n, "Albums added", sep=' ')
    close_connection(cursor, conn)


def add_artists(n):
    cursor, conn = open_connection()
    gen_artists = ArtistGenerator()
    gen_artists.get_primary_key_data(n)
    for a in gen_artists.data:
        params = gen_artists.get_params()
        print(a, params, sep=': ')
        cursor.execute(
            'insert into artist (name, "desc", country, icon_path, "group") values (%s, %s, %s, %s, %s);commit;',
            (a, params.get('desc'), params.get('country'), params.get('icon_path'), params.get('group')))
    print(n, "Artists added", sep=' ')
    close_connection(cursor, conn)


def add_groups(n):
    cursor, conn = open_connection()
    gen_groups = GroupGenerator()
    gen_groups.get_primary_key_data(n)
    for g in gen_groups.data:
        params = gen_groups.get_params()
        print(g, params, sep=': ')
        cursor.execute('insert into "group"(name, "desc", country, icon_path) values(%s, %s, %s, %s);commit;',
                       (g, params.get('desc'), params.get('country'), params.get('icon_path')))
    print(n, "Records added", sep=' ')
    close_connection(cursor, conn)


def add_users(n):
    cursor, conn = open_connection()
    gen_users = UserGenerator()
    gen_users.get_primary_key_data(n)
    for u in gen_users.data:
        params = gen_users.get_params()
        print(u, params, sep=': ')
        cursor.execute('insert into "user" (email, name, icon_path, password) values(%s, %s, %s, %s);commit;',
                       (u, params.get('name'), params.get('icon_path'), params.get('password')))
    print(n, "Records added", sep=' ')
    close_connection(cursor, conn)


def add_playlists_table():
    cursor, conn = open_connection()
    cursor.execute('SELECT count(*) FROM playlist;')
    length_playlist = cursor.fetchone()[0]
    cursor.execute('SELECT count(*) FROM song;')
    length_song = cursor.fetchone()[0]
    for i in range(0, int(length_song / 4)):
        cursor.execute('insert into playlists_table (playlist, song) VALUES (%s, %s);',
                       (random.randint(0, length_playlist - 1), random.randint(0, length_song - 1)))
    close_connection(cursor, conn)


def add_groups_table():
    cursor, conn = open_connection()
    cursor.execute('SELECT count(*) FROM song;')
    length_song = cursor.fetchone()[0]
    for i in range(0, int(length_song / 4)):
        cursor.execute('SELECT name FROM "group" ORDER BY RANDOM() LIMIT 1;')
        creator = cursor.fetchone()
        print(creator)
        cursor.execute('insert into groups_table (creator, song) VALUES (%s, %s);commit;',
                       (creator, random.randint(0, length_song - 1)))
    close_connection(cursor, conn)


def add_artists_table():
    cursor, conn = open_connection()
    cursor.execute('SELECT count(*) FROM song;')
    length_song = cursor.fetchone()[0]
    for i in range(0, int(length_song / 4)):
        cursor.execute('SELECT name FROM "artist" ORDER BY RANDOM() LIMIT 1;')
        creator = cursor.fetchone()
        print(creator)
        cursor.execute('insert into artists_table (creator,song) VALUES (%s, %s);commit;',
                       (creator, random.randint(0, length_song - 1)))
    close_connection(cursor, conn)


def add_likes():
    cursor, conn = open_connection()
    cursor.execute('SELECT count(*) FROM "user";')
    length_user = cursor.fetchone()[0]
    cursor.execute('SELECT count(*) FROM album;')
    length_album = cursor.fetchone()[0]
    cursor.execute('SELECT count(*) FROM song;')
    length_song = cursor.fetchone()[0]
    cursor.execute('SELECT count(*) FROM playlist;')
    length_playlist = cursor.fetchone()[0]
    for i in range(0, int(length_user / 4)):
        cursor.execute('SELECT email FROM "user" ORDER BY RANDOM() LIMIT 1;')
        user = cursor.fetchone()
        cursor.execute('SELECT name FROM "group" ORDER BY RANDOM() LIMIT 1;')
        group = cursor.fetchone()
        cursor.execute('insert into like_song ("user",song) VALUES (%s, %s);commit;',
                       (user, random.randint(0, length_song - 1)))
        cursor.execute('insert into like_album ("user",album) VALUES (%s, %s);commit;',
                       (user, random.randint(0, length_album - 1)))
        cursor.execute('insert into like_group ("user","group") VALUES (%s, %s);commit;',
                       (user, group))
        cursor.execute('insert into like_playlist ("user",playlist) VALUES (%s, %s);commit;',
                       (user, random.randint(0, length_playlist - 1)))
    close_connection(cursor, conn)


def add_songs_area(n):
    add_albums(n)
    add_songs(n)
    add_playlists(n)
    add_playlists_table()


def add_groups_area(n):
    add_groups(n)
    add_artists(n)
    add_groups_table()
    add_artists_table()


def add_users_area(n):
    add_users(n)
    add_likes()


def add_all(n):
    add_songs_area(n)
    add_groups_area(n)
    add_users_area(n)
