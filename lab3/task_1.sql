select a.creator,
       num_of_songs,
       num_of_song_with_group,
       num_of_songs - num_of_song_with_group                                                          as num_of_song_without_group,
       cast((num_of_songs - num_of_song_with_group) as real) / cast((num_of_song_with_group) AS REAL) as res
from (select art.creator, count(a.name) as num_of_song_with_group
      from artist a
               join artists_table art on a.name = art.creator
               join song s on art.song = s.id
               join history_artist_table ht on a.name = ht.artist
               join "group" g on ht."group" = g.name
      where s.year between ht.start_date and ht.end_date
      group by art.creator
     ) a
         join
     -- все песни артиста
         (select creator
               , count(artists_table.song) as num_of_songs
          from artists_table
          group by creator) b
     on a.creator = b.creator
where num_of_song_with_group > 0
order by res desc
limit 5;