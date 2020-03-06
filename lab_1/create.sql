start transaction;

drop table if exists "group", artists_table, groups_table;
create table "group"
(
    name      varchar(255) primary key not null,
    "desc"    varchar(255),
    country   varchar(255),
    icon_path varchar(255)
);

drop table if exists artist, songs_table, like_song, album, song, songs_table, groups_table, playlists_table,
    like_album, like_artist;
create table artist
(
    name      varchar(255) primary key not null,
    "desc"    varchar(255),
    country   varchar(255),
    icon_path varchar(255)
);

drop table if exists album, like_album, song;
create table album
(
    id        integer primary key                   not null,
    name      varchar(255)                          not null,
    year      integer                               not null,
    duration  time                                  not null,
    quantity  integer                               not null,
    icon_path varchar(255)                          not null,
    artist    varchar(255) references artist (name) not null
);

drop table if exists artists_table;
create table artists_table
(
    group_id  varchar(255) references "group" (name) not null,
    artist_id varchar(255) references artist (name)  not null
);

drop table if exists song;
create table song
(
    id       integer primary key not null,
    name     varchar(255)        not null,
    path     varchar(255)        not null,
    album_id integer references album (id)
);

drop table if exists groups_table;
create table groups_table
(
    group_id varchar(255) references "group" (name) not null,
    song_id  integer references song (id)           not null
);



drop table if exists songs_table;
create table songs_table
(
    artist_id varchar(255) references artist (name) not null,
    song_id   integer references song (id)          not null
);



drop table if exists playlist, like_playlist;
create table playlist
(
    id        integer primary key not null,
    name      varchar(255)        not null,
    quantity  integer             not null,
    author    varchar(255)        not null,
    duration  time                not null,
    icon_path varchar(255)        not null
);

drop table if exists playlists_table;
create table playlists_table
(
    playlist_id integer references playlist (id) not null,
    song_id     integer references song (id)     not null
);

drop table if exists "user";
create table "user"
(
    email     varchar(255) primary key not null,
    name      varchar(255)             not null,
    icon_path varchar(255),
    password  varchar(255)             not null

);

drop table if exists like_song;
create table like_song
(
    user_id varchar(255) references "user" (email) not null,
    song_id integer references song (id)           not null
);

drop table if exists like_album;
create table like_album
(
    user_id  varchar(255) references "user" (email) not null,
    album_id integer references album (id)          not null
);

drop table if exists like_artist;
create table like_artist
(
    user_id   varchar(255) references "user" (email) not null,
    artist_id varchar(255) references artist (name)  not null
);

drop table if exists like_playlist;
create table like_playlist
(
    user_id     varchar(255) references "user" (email) not null,
    playlist_id integer references playlist (id)       not null
);

commit;