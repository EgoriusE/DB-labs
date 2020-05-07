def delete_users_area(cursor):
    cursor.execute('delete from like_song;')
    cursor.execute('delete from like_album;')
    cursor.execute('delete from like_group;')
    cursor.execute('delete from like_playlist;')
    cursor.execute('delete from "user";')


def delete_prizers_area(cursor):
    cursor.execute('delete from prizes_songs_table;')
    cursor.execute('delete from prizes_albums_table;')
    cursor.execute('delete from prize;')


def delete_groups_area(cursor):
    cursor.execute('delete from history_artist_table')
    cursor.execute('delete from groups_table')
    cursor.execute('delete from artists_table')
    cursor.execute('delete from artist;')
    cursor.execute('delete from "group";')


def delete_songs_area(cursor):
    cursor.execute('delete from playlists_table;')
    cursor.execute('delete from playlist;')
    cursor.execute('delete from song;')
    cursor.execute('delete from album;')
