query_1 = "select email, " \
          "name," \
          "ls.song as like_song_id," \
          "la.album as like_album_id," \
          "lg.\"group\"  as like_group_name," \
          "lp.playlist as like_playlit_id " \
          "from \"user\"" \
          "join like_song ls on \"user\".email = ls.\"user\"" \
          "join like_album la on \"user\".email = la.\"user\" " \
          "join like_group lg on \"user\".email = lg.\"user\" " \
          "join like_playlist lp on \"user\".email = lp.\"user\";"

query_2 = "select * " \
          "from playlists_table " \
          "left join playlist p on playlists_table.playlist = p.id " \
          "join song s on playlists_table.song = s.id " \
          "where playlists_table.playlist = 1813;"

query_3 = "select public.album.id, name, year, prize " \
          "from album " \
          "right join prizes_albums_table pat on album.id = pat.album " \
          "where public.album.type = 'concert';"

query_4 = "select id, name, year, a.creator, gt.creator " \
          "from song " \
          "right join artists_table a on song.id = a.song " \
          "right join groups_table gt on song.id = gt.song " \
          "where song.year between 1970 and 2000;"

query_5 = "select name, count(*) as num_of_songs " \
          "from artist " \
          "right join artists_table a on artist.name = a.creator " \
          "group by name " \
          "order by num_of_songs desc;"

query_6 = "select email, name, count(*) as num_of_like_songs " \
          "from \"user\" " \
          "right join like_song ls on \"user\".email = ls.\"user\"" \
          " group by email, name " \
          "having count(*) > 1" \
          " order by num_of_like_songs desc;"

query_list = (query_1, query_2, query_3, query_4, query_5, query_6)
