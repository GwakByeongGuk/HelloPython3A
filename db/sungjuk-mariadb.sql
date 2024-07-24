drop table sungjuk;

create table sungjuk (
                         sjno integer primary key auto_increment,
                         name varchar(10) not null,
                         kor  int not null,
                         eng  int not null,
                         mat  int not null,
                         tot  int not null,
                         avg  decimal(5,1),
                         grd  varchar(2),
                         #regdate datetime default now()
                             regdate datetime default current_timestamp
);

insert into sungjuk (name, kor, eng, mat, tot, avg, grd)
values ('abc123', 99, 99, 99, 297, 99.0, '수');

select * from sungjuk;