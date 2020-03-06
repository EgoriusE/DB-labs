start transaction;

insert into artist (name, "desc", country, icon_path)
values ('Скриптонит', null, null, 'D:\store\artist\Скриптонит.png');
insert into artist (name, "desc", country, icon_path)
values ('Rem Digga', null, null, 'D:\store\artist\Maqlao.png');
insert into artist (name, "desc", country, icon_path)
values ('MiyaGi & Эндшпиль', null, null, 'D:\store\artist\MiyaGi & Эндшпиль.png');
insert into artist (name, "desc", country, icon_path)
values ('Pizza', null, null, 'D:\store\artist\Pizza.png');
insert into artist (name, "desc", country, icon_path)
values ('Matrang', null, null, 'D:\store\artist\Matrang.png');
insert into artist (name, "desc", country, icon_path)
values ('Frank Sinatra', null, null, 'D:\store\artist\Frank Sinatra.png');

insert into album (id, name, year, duration, quantity, icon_path, artist)
values (1, 'Хит-коктейль. Осень 2018', 2017, '01:37', 25, 'D:\store\album\1.png', 'MiyaGi & Эндшпиль');
insert into album (id, name, year, duration, quantity, icon_path, artist)
values (2, 'Молодежка', 2015, '00:54', 15, 'D:\store\album\2.png', 'Pizza');
insert into album (id, name, year, duration, quantity, icon_path, artist)
values (3, 'От луны до Марса', 2018, '00:04', 1, 'D:\store\album\3.png', 'Matrang');
insert into album (id, name, year, duration, quantity, icon_path, artist)
values (4, '2004', 2019, '01:00', 24, 'D:\store\album\4.png', 'Скриптонит');
insert into album (id, name, year, duration, quantity, icon_path, artist)
values (5, 'Thats life', 1966, '00:25', 10, 'D:\store\album\5.png', 'Frank Sinatra');

insert into song (id, name, path, album_id)
values (1, 'I Got Love', 'D:\store\songs\2.mp3', 1);
insert into song (id, name, path, album_id)
values (2, 'Лифт', 'D:\store\songs\3.mp3', 2);
insert into song (id, name, path, album_id)
values (3, 'От луны до марса', 'D:\store\songs\4.mp3', 3);
insert into song (id, name, path, album_id)
values (4, 'Москва любит...', 'D:\store\songs\5.mp3', 4);
insert into song (id, name, path, album_id)
values (5, 'Привычка', 'D:\store\songs\6.mp3', 4);
insert into song (id, name, path, album_id)
values (6, 'Thats life', 'D:\store\songs\7.mp3', 5);

insert into songs_table (artist_id, song_id)
values ('MiyaGi & Эндшпиль', 1);
insert into songs_table (artist_id, song_id)
values ('Pizza', 2);
insert into songs_table (artist_id, song_id)
values ('Matrang', 3);
insert into songs_table (artist_id, song_id)
values ('Скриптонит', 4);
insert into songs_table (artist_id, song_id)
values ('Скриптонит', 5);

insert into "user" (email, name, icon_path, password)
values ('egorius.belov@yandex.com', 'egorius', 'D:\store\users\egorius.belov.png,', '1234');
insert into "user" (email, name, icon_path, password)
values ('ega.bel99@gmail.com', 'bobrusik', 'D:\store\users\ega.bel99.png,', '12345678');

insert into like_song (user_id, song_id)
values ('egorius.belov@yandex.com', 1);
insert into like_song (user_id, song_id)
values ('egorius.belov@yandex.com', 2);
insert into like_song (user_id, song_id)
values ('egorius.belov@yandex.com', 3);

insert into like_artist (user_id, artist_id)
values ('ega.bel99@gmail.com', 'Скриптонит');
commit;