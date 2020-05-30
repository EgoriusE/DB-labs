import random
import threading
import time

import matplotlib.pyplot as plt

from ConstantsQeuries import query_1, query_2, query_3, query_4, query_5, query_6, query_list
from Utils import open_connection, drop_index

connection, cursor = open_connection()

curr_res_constant_threads = [[]]
curr_res_dynamic_threads = []
cursor.execute("select \"user\" from like_song;")
like_song_email = cursor.fetchall()
cursor.execute("select \"user\" from like_album;")
like_album_email = cursor.fetchall()
cursor.execute("select \"user\" from like_group;")
like_group_email = cursor.fetchall()
cursor.execute("select \"user\" from like_playlist;")
like_playlist_email = cursor.fetchall()
cursor.execute("select song from playlists_table;")
playlist_table_songs = cursor.fetchall()
cursor.execute("select album from prizes_albums_table;")
prizes_albums = cursor.fetchall()
cursor.execute("select id from song;")
songs_ids = cursor.fetchall()
cursor.execute("select name from \"group\";")
group_names = cursor.fetchall()
cursor.execute("select song from artists_table;")
art_songs = cursor.fetchall()
cursor.execute("select song from groups_table;")
grp_songs = cursor.fetchall()
cursor.execute("select \"group\" from history_artist_table;")
h_group = cursor.fetchall()
cursor.execute("select creator from artists_table;")
at_creator = cursor.fetchall()

before = True


def main():
    drop_index()
    check_explain_analyze()
    # constant_threads(1)
    # constant_threads(2)
    # dinamic_threads(200)
    optimize()
    check_explain_analyze()
    # constant_threads(1)
    # constant_threads(2)
    dinamic_threads(200)


def constant_threads(num_threads):
    curr_res_constant_threads.clear()
    for t in range(num_threads):
        dbt = DBThread_constant_threads(t)
        dbt.start()
    while threading.activeCount() > 1:
        time.sleep(1)
    plot_x = [k for k in range(401, 10000, 400)]
    plot_y = []
    for i in range(len(curr_res_constant_threads[0])):
        curr_sum = 0
        for j in range(num_threads):
            curr_sum += curr_res_constant_threads[j][i]
        plot_y.append(curr_sum / num_threads)
    plt.plot(plot_x, plot_y, linewidth=2.0)
    plt.xlabel('Запросов в секунду')
    plt.ylabel('Время ответа на один запрос, мс')
    if before:
        plt.title("Before. Num threads: {}".format(num_threads))
    else:
        plt.title("After. Num threads: {}".format(num_threads))
    plt.show()


def dinamic_threads(num_querys):
    plot_x = [k for k in range(1, 31)]
    plot_y = []
    for num_threads in range(1, 31):
        curr_res_dynamic_threads.clear()
        for t in range(num_threads):
            dbt = DBThread_dynamic_threads(num_querys)
            dbt.start()

        while threading.activeCount() > 1:
            time.sleep(1)

        plot_y.append(sum(curr_res_dynamic_threads) / len(curr_res_dynamic_threads))

    plt.plot(plot_x, plot_y, linewidth=2.0)
    plt.xlabel('Количество потоков')
    plt.ylabel('Время ответа на один запрос, мс')
    if before:
        plt.title("Before. Dynamic thread num")
    else:
        plt.title("After. Dynamic thread num")
    plt.show()


def optimize():
    cursor.execute("create  index us_ind_1 on like_song(\"user\");")
    cursor.execute("create  index us_ind_2 on like_album(\"user\");")
    cursor.execute("create index  us_ind_3 on like_group(\"user\");")
    cursor.execute("create  index pl_id on playlists_table(playlist) where playlist=1813;")
    cursor.execute("create index album_type_ind on album(type) where type = 'concert';")
    cursor.execute("create index song_id_ind on song(year) where year between 1970 and 2000;commit;")
    cursor.execute("create index user_email_ind on like_song(\"user\") ;commit ;")
    cursor.execute("create index artists_id on artists_table(creator);commit;")
    global before
    before = False
    print(before)


def exec_query_before(query, thread_cursor):
    if query == query_1:
        thread_cursor.execute("EXPLAIN ANALYZE " + query_1)
    elif query == query_2:
        thread_cursor.execute("EXPLAIN ANALYZE " + query_2)
    elif query == query_3:
        thread_cursor.execute("EXPLAIN ANALYZE " + query_3)
    elif query == query_4:
        thread_cursor.execute("EXPLAIN ANALYZE " + query_4)
    elif query == query_5:
        thread_cursor.execute("EXPLAIN ANALYZE " + query_5)
    elif query == query_6:
        thread_cursor.execute("EXPLAIN ANALYZE " + query_6)
    else:
        print("Wrong query!")
    fetch_res = thread_cursor.fetchall()
    try:
        return float(fetch_res[-1][0].split(" ")[2]) + float(fetch_res[-2][0].split(" ")[2])
    except ValueError:
        return float(fetch_res[-1][0].split(" ")[2]) + float(fetch_res[-2][0].split(" ")[4].split("=")[1]) + float(
            fetch_res[-3][0].split(" ")[2])


def exec_query_after(query, thread_cursor):
    if query == query_1:
        thread_cursor.execute("EXPLAIN ANALYZE EXECUTE query1 (%s,%s,%s,%s);",
                              (random.choice(like_song_email), random.choice(like_album_email),
                               random.choice(like_group_email), random.choice(like_playlist_email)))
    elif query == query_2:
        thread_cursor.execute("EXPLAIN ANALYZE EXECUTE query2 (%s,%s);", (5884, random.choice(playlist_table_songs)))
    elif query == query_3:
        thread_cursor.execute("EXPLAIN ANALYZE EXECUTE query3 (%s);", random.choice(prizes_albums))
    elif query == query_4:
        thread_cursor.execute("EXPLAIN ANALYZE EXECUTE query4 (%s);", (random.choice(art_songs)))
    elif query == query_5:
        thread_cursor.execute("EXPLAIN ANALYZE EXECUTE query5 (%s);", random.choice(at_creator))
    elif query == query_6:
        thread_cursor.execute("EXPLAIN ANALYZE EXECUTE query6 (%s);", random.choice(like_song_email))
    else:
        print("Wrong query!")
    fetch_res = thread_cursor.fetchall()
    try:
        # print(float(fetch_res[-1][0].split(" ")[2]) + float(fetch_res[-2][0].split(" ")[2]))
        return float(fetch_res[-1][0].split(" ")[2]) + float(fetch_res[-2][0].split(" ")[2])
    except ValueError:
        return float(fetch_res[-1][0].split(" ")[2]) + float(fetch_res[-2][0].split(" ")[4].split("=")[1]) + float(
            fetch_res[-3][0].split(" ")[2])


def check_explain_analyze():
    cursor.execute("EXPLAIN ANALYZE " + query_1)
    print(cursor.fetchall())


class DBThread_constant_threads(threading.Thread):
    def __init__(self, curr_thread):

        self.curr_thread = curr_thread
        threading.Thread.__init__(self)
        self.conn, self.cur = open_connection()

        global before
        if not before:
            self.cur.execute(
                "prepare query1 (varchar) as select email, name,ls.song     as like_song_id,la.album    as "
                "like_album_id,lg.\"group\"  as like_group_name,lp.playlist as like_playlit_id from \"user\" join "
                "like_song ls on \"user\".email = $1 join like_album la on \"user\".email = $2 join like_group lg on "
                "\"user\".email = $3 join like_playlist lp on \"user\".email = $4;")
            self.cur.execute(
                "prepare query2 as select * from playlists_table left join playlist p on playlists_table.playlist = "
                "p.id join song s on playlists_table.song = $2     where playlists_table.playlist = $1;")
            self.cur.execute(
                "prepare query3 (int) as select public.album.id, name, year, prize from album right join "
                "prizes_albums_table pat on album.id = $1 where public.album.type = 'concert';")
            self.cur.execute(
                "prepare query4 (int) as select id, name, year, a.creator, gt.creator from song right join "
                "artists_table a on song.id = $1 right join groups_table gt on song.id = gt.song where song.year "
                "between 1970 and 2000;")
            self.cur.execute(
                "prepare query5(varchar) as select name, count(*) as num_of_songs from artist right join "
                "artists_table a on artist.name = $1 group by name order by num_of_songs desc;")
            self.cur.execute(
                "prepare query6 (varchar) as select email, name, count(*) as num_of_like_songs from \"user\" right "
                "join like_song ls on \"user\".email = $1 group by email, name having count(*) > 1 order by "
                "num_of_like_songs desc;")

    def run(self):
        for i in range(401, 10000, 400):
            results = []
            for j in range(0, i):
                random_query = random.choice(query_list)
                if before:
                    results.append(exec_query_before(random_query, self.cur))
                else:
                    results.append(exec_query_after(random_query, self.cur))
            if len(curr_res_constant_threads) < self.curr_thread + 1:
                curr_res_constant_threads.append([])
            curr_res_constant_threads[self.curr_thread].append(sum(results) / len(results))
            print(i)
        self.conn.commit()


class DBThread_dynamic_threads(threading.Thread):
    def __init__(self, num_querys):

        self.num_querys = num_querys
        threading.Thread.__init__(self)
        self.conn, self.cur = open_connection()

        global before
        if not before:
            self.cur.execute(
                "prepare query1 (varchar) as select email,name,ls.song     as like_song_id,la.album    as "
                "like_album_id,lg.\"group\"  as like_group_name,lp.playlist as like_playlit_id from \"user\" join "
                "like_song ls on \"user\".email = $1 join like_album la on \"user\".email = $2 join like_group lg on "
                "\"user\".email = $3 join like_playlist lp on \"user\".email = $4;")
            self.cur.execute(
                "prepare query2 as select * from playlists_table left join playlist p on playlists_table.playlist = "
                "p.id join song s on playlists_table.song = $2     where playlists_table.playlist = $1;")
            self.cur.execute(
                "prepare query3 (int) as select public.album.id, name, year, prize from album right join "
                "prizes_albums_table pat on album.id = $1 where public.album.type = 'concert';")
            self.cur.execute(
                "prepare query4 (int) as select id, name, year, a.creator, gt.creator from song right join "
                "artists_table a on song.id = $1 right join groups_table gt on song.id = $1 where song.year between "
                "1970 and 2000;")
            self.cur.execute(
                "prepare query5 (varchar) as select name, count(*) as num_of_songs from artist right join "
                "artists_table a on artist.name = $1 group by name order by num_of_songs desc;")
            self.cur.execute(
                "prepare query6 (varchar) as select email, name, count(*) as num_of_like_songs from \"user\" right "
                "join like_song ls on \"user\".email = $1 group by email, name having count(*) > 1 order by "
                "num_of_like_songs desc;")

    def run(self):
        results = []
        for j in range(0, self.num_querys + 1):
            print(j)
            random_query = random.choice(query_list)
            if before:
                results.append(exec_query_before(random_query, self.cur))
            else:
                results.append(exec_query_after(random_query, self.cur))
        curr_res_dynamic_threads.append(sum(results) / len(results))
        self.conn.commit()


if __name__ == "__main__":
    main()
