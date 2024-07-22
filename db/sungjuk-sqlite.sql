
---  console로 테이블만들기  / sungjuk-sqlite.sql  (db폴더에 만들기)

create table sungjuk(
                        sjno    integer  primary key autoincrement,
                        name    varchar(20)     not null,
                        kor     int             not null,
                        eng     int             not null,
                        mat     int             not null,
                        tot     int             not null,
                        avg     decimal(5,1),
                        grd     varchar(2)     not null,
    -- regdate datetime default (datetime('now'))   -- UTC
                        regdate datetime default (datetime('now', 'localtime')) -- UTC+9
);

INSERT INTO SungJuk (name, kor, eng, mat, tot, avg, grd)
VALUES ('abc123', 99, 99, 99, 297, 99.0, '수');

-- 성적 데이터 중 이름으로 조회
select * from sungjuk where name = 'abc123';
-- 성적 데이터 중 등록일만 조회
select sjno,name,kor,eng,mat,substr(regdate,0,11) from sungjuk;
-- 성적 데이 터중 학생번호 로 조회
select * from sungjuk where sjno = 1;


select * from sungjuk