drop table sungjuk;

-- 성적 테이블 생성
create table sungjuk (
                         sjno integer primary key autoincrement,
                         name varchar(10) not null,
                         kor  int not null,
                         eng  int not null,
                         mat  int not null,
                         tot  int not null,
                         avg  decimal(5,1),
                         grd  varchar(2),
    -- regdate datetime default (datetime('now'))  -- UTC
                         regdate datetime default (datetime('now', 'localtime'))  -- UTC + 9
);

-- 성적 데이터 추가
insert into sungjuk (name, kor, eng, mat, tot, avg, grd)
values ('abc123', 99, 99, 99, 297, 99.0, '수');

-- 성적 데이터 전체 조회
select * from sungjuk;

-- 성적 데이터 중 이름,국어,영어,수학만 조회
select name,kor,eng,mat from sungjuk;

-- 성적 데이터 중 학생번호,이름,국어,영어,수학,등록일만 조회
select
    sjno,name,kor,eng,mat,substr(regdate,0,11) regdate
from sungjuk;

-- 성적 데이터 중 이름으로 검색해서 모두 조회
select * from sungjuk where name = 'abc123';

-- 성적 데이터 중 학생번호로 검색해서 모두 조회
select * from sungjuk where sjno = 1;

-- 성적 데이터 총 갯수 조회
-- select count(*) total from sungjuk;
-- select count(name) total from sungjuk;
select count(sjno) total from sungjuk;