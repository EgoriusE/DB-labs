-- 1. Сделайте выборку всех данных из каждой таблицы
select *
from album;
select *
from artist;
select *
from artists_table;
select *
from "group";
select *
from groups_table;
select *
from history_artist_table;
select *
from like_album;
select *
from like_group;
select *
from like_playlist;
select *
from like_song;
select *
from playlist;
select *
from playlists_table;
select *
from prize;
select *
from prizes_albums_table;
select *
from prizes_songs_table;
select *
from song;
select *
from "user";

-- 2. Сделайте выборку данных из одной таблицы при нескольких условиях, с использованием логических операций, LIKE, BETWEEN, IN
select email, name
from "user"
where email like '%yahoo%';

select id, name, year
from song
where year between 1990 and 2010;

select *
from album
where year in (2007, 2010, 2015);

-- 3. Создайте в запросе вычисляемое поле
select id, name 'средняя длительность песни', (duration / quantity)
from playlist;

-- 4. Сделайте выборку всех данных с сортировкой по нескольким полям
select *
from playlist
order by quantity, duration;

-- 5. Создайте запрос, вычисляющий несколько совокупных характеристик таблиц
select name, count(*) as num_of_names
from "user"
where email like '%yandex%'
group by name
order by name;

-- 6. Сделайте выборку данных из связанных таблиц (не менее двух примеров)
select "group".name, country, groups_table.song, hat.artist
from "group"
         join groups_table on "group".name = groups_table.creator
         join history_artist_table hat on "group".name = hat."group";

select pst.song, prize.id as prize_id
from prize
         right join prizes_songs_table pst on prize.id = pst.prize;

-- 7. Создайте запрос, рассчитывающий совокупную характеристику с использованием группировки, наложите ограничение на результат группировки
select hat.start_date, count(*) as num_of_start_date
from artist
         join history_artist_table hat on artist.name = hat.artist
group by hat.start_date
having count(*) > 1;


-- 8. Придумайте и реализуйте пример использования вложенного запроса
select id, name
from song
where album in
      (select id
       from album
       where type = 'compilation');

-- 9. С помощью оператора INSERT добавьте в каждую таблицу по одной записи
insert into song (id, name, path, album, year)
values ((select count(*) from song) + 1, 'My Love', 'D/songs/mylove.mp3',
        (select id from album order by random() limit 1), 2019);

insert into album (id, name, year, duration, quantity, icon_path, type)
values ((select count(*) from album) + 1, 'album', 2017, '01:37', 25, 'D:\store\album\1.png', 'album');

insert into groups_table (song, creator)
values ((select id from song order by random() limit 1), (select name from "group" order by random() limit 1));

insert into artists_table (song, creator)
values ((select id from song order by random() limit 1), (select name from artist order by random() limit 1));

insert into playlist (id, name, quantity, author, duration, icon_path)
values ((select count(*) from song) + 1, 'df', 10, 'ff', '11:33', 'D:\store\album\1.png');

insert into playlists_table (playlist, song)
values ((select id from playlist order by random() limit 1), (select id from song order by random() limit 1));

-- 10. С помощью оператора UPDATE измените значения нескольких полей у всех записей, отвечающих заданному условию
update album
set year     = 2020,
    quantity = 10
where type = 'concert';

-- 11. С помощью оператора DELETE удалите запись, имеющую максимальное (минимальное) значение некоторой совокупной характеристики
delete
from song
where year = (select max(year) from song);


-- 12. С помощью оператора DELETE удалите записи в главной таблице,
-- на которые не ссылается подчиненная таблица (используя вложенный запрос)
delete from prize where id not in (select prize from prizes_songs_table);