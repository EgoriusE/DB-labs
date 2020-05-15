select sum_gr.name_gr        as group_name,
       sum_gr.num_gr_prize   as num_of_songs_with_prize_in_group,
       sum_art.num_prize_art as num_of_songs_with_prize_artist
from (select name_gr, count(prize_art) as num_gr_prize
      from (select g.name as name_gr, song
            From artist a
                     join history_artist_table hat on a.name = hat.artist
                     join artists_table art on a.name = art.creator
                     Left join song s on art.song = s.id
                     join "group" g on hat."group" = g.name
            Where year between start_date and end_date) d
               Left join
           --  количество  наград у песни
               (Select song
                     , Count(prizes_songs_table.prize) as prize_art
                From prizes_songs_table
                group by song) e
           On d.song = e.song
      Group by name_gr) sum_gr
         join
     (
         Select name_gr, count(prize_art) as num_prize_art
         From
--     — считаем все награды у исполнителя вне группы
(select g.name as name_gr, song
 From artist a
          join history_artist_table hat on a.name = hat.artist
          join artists_table art on a.name = art.creator
          Left join song s on art.song = s.id
          join "group" g on hat."group" = g.name
 Where year not between start_date and end_date) c
    Left join
--     — количество наград у песни
    (Select song, Count(prizes_songs_table.prize) as prize_art
     From prizes_songs_table
     group by song) b
On c.song = b.song
         Group by name_gr) sum_art
     on sum_gr.name_gr = sum_art.name_gr
Where num_gr_prize > num_prize_art;