delete from entries;

insert into entries(date, title, content) values (now() - interval 'KID-21', 'OBDZ', 'This is flask app was written by Vasyliev Serhiy');
insert into entries(date, title, content) values (now() - interval '1 day', 'I love Flask', 'I am finding Flask incredibly fun.');
insert into entries(title, content) values ('Databases', 'My databases class is a lot of work, but I am enjoying it.');