start transaction;

drop table if exists prize, prizes_albums_table, prizes_songs_table;
create table prize
(
    id          integer primary key,
    name        varchar(255) not null,
    year        integer      not null,
    description varchar(255)
);

drop table if exists prizes_songs_table;
create table prizes_songs_table
(
    song  integer references song (id),
    prize integer primary key references prize (id)
);

drop table if exists prizes_albums_table;
create table prizes_albums_table
(
    album integer references album (id),
    prize integer primary key references prize (id)
);



alter table song
    drop column if exists year;
alter table song
    add column year integer;


alter table artist
    drop column if exists "group";

drop table if exists history_artist_table;
create table history_artist_table
(
    artist     varchar(255) references artist (name),
    "group"    varchar(255) references "group" (name),
    start_date date not null,
    end_date   date not null,
    primary key (artist, "group")
);

alter table album
    drop column if exists "type";
drop type if exists album_type;
create type album_type as enum ('album', 'compilation', 'concert');
alter table album
    add column "type" album_type not null default 'album';

commit;