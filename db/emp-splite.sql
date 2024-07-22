-- 테이블 추가
CREATE TABLE emp (
         empid integer primary key,
         fname varchar(40) not null,
         lname varchar(40) not null,
         email varchar(40) not null,
         phone varchar(40) not null,
         hdate date not null,
         jobid varchar(40) not null,
         sal integer,
         comm decimal(5,2),
         mgrid integer,
         deptid integer
);

-- 데이터 추가
insert into emp (empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)
values (100,'Steven','King','SKING','515.123.4567','2003-06-17','AD_PRES',24000,null,null,90);

-- 데이터 조회1 - 리스트
select empid,fname,email,jobid,deptid from emp;

-- 데이터 조회2 - 상세
select * from emp where empid = 100;