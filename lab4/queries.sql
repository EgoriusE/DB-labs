-- 1.

drop index if exists us_ind_1;
drop index if exists us_ind_2;
drop index if exists us_ind_3;

explain analyze
select email,
       name,
       ls.song     as like_song_id,
       la.album    as like_album_id,
       lg."group"  as like_group_name,
       lp.playlist as like_playlit_id
from "user"
         join like_song ls on "user".email = ls."user"
         join like_album la on "user".email = la."user"
         join like_group lg on "user".email = lg."user"
         join like_playlist lp on "user".email = lp."user";


create index us_ind_1 on like_song ("user");
create index us_ind_2 on like_album ("user");
create index us_ind_3 on like_group ("user");
prepare query1 (varchar) as select email,
                                   name,
                                   ls.song     as like_song_id,
                                   la.album    as like_album_id,
                                   lg."group"  as like_group_name,
                                   lp.playlist as like_playlit_id
                            from "user"
                                     join like_song ls on "user".email = $1
                                     join like_album la on "user".email = $2
                                     join like_group lg on "user".email = $3
                                     join like_playlist lp on "user".email = $4;
explain analyze execute query1('blacklegging1968@outlook.com',
    'scorner2026@live.com', 'alcalde1839@yahoo.com', 'debatement1813@yahoo.com');


-- 2. 

drop index if exists pl_id;

explain analyze
select *
from playlists_table
         left join playlist p on playlists_table.playlist = p.id
         join song s on playlists_table.song = s.id
where playlists_table.playlist = 5884;


create index pl_id on playlists_table (playlist) where playlist = 5884;
prepare query2 as
    select *
    from playlists_table
             left join playlist p on playlists_table.playlist = p.id
             join song s on playlists_table.song = $2
    where playlists_table.playlist = $1;
explain analyze execute query2(5884,1 );


-- 3. 

drop index if exists album_type_ind;

explain analyze
select public.album.id, name, year, prize
from album
         right join prizes_albums_table pat on album.id = pat.album
where public.album.type = 'concert';


create index album_type_ind on album (type) where type = 'concert';
prepare query3 (int) as
    select public.album.id, name, year, prize
    from album
             right join prizes_albums_table pat on album.id = $1
    where public.album.type = 'concert';
explain analyze execute query3(8533);


-- 4.

drop index if exists song_id_ind;

explain analyze
select id, name, year, a.creator, gt.creator
from song
         right join artists_table a on song.id = a.song
         right join groups_table gt on song.id = gt.song
where song.year between 1970 and 2000;


create index song_id_ind on song (year) where year between 1970 and 2000;
commit;
prepare query4 (int) as
    select id, name, year, a.creator, gt.creator
    from song
             right join artists_table a on song.id = $1
             right join groups_table gt on song.id = gt.song
    where song.year between 1970 and 2000;
explain analyze execute query4(257);

-- 5.

drop index if exists artists_id;

explain analyze
select name, count(*) as num_of_songs
from artist
         right join artists_table a on artist.name = a.creator
group by name
order by num_of_songs desc;


create index artists_id on artists_table(creator);
prepare query5(varchar) as
    select name, count(*) as num_of_songs
    from artist
             right join artists_table a on artist.name = $1
    group by name
    order by num_of_songs desc;
explain analyze execute query5(413.9376021530718);


-- 6. 

create index user_email_ind on like_song ("user");

drop index if exists user_email_ind;
explain analyze
select email, name, count(*) as num_of_like_songs
from "user"
         right join like_song ls on "user".email = ls."user"
group by email, name
having count(*) > 1
order by num_of_like_songs desc;

prepare query6 (varchar) as select email, name, count(*) as num_of_like_songs
                            from "user"
                                     right join like_song ls on "user".email = $1
                            group by email, name
                            having count(*) > 1
                            order by num_of_like_songs desc;
explain analyze execute query6('subcostae2058@yandex.com');
