# 파이썬 데이터베이스 프로그래밍
# 파이썬에서는 일박적인 관계형 데이터베이스를 이용해서
# 데이터를 저장,검색,수정,삭제할 수 있음
# 또한, 독립적인 데이터베이스 서버없이, 파일기반
# 데이터베이스를 이용해서 간편하게 데이터를 조작할 수도 있음
# 내장형 파일기반 데이터베이스 : sqlite

# sqlite
# 내장형 파일기반 데이터베이스
# 서버가 필요없고 복잡한 설정도 필요없으면서
# 트랜잭션이 지원되는 데이터베이스
# 하나의 파일에 테이블,뷰,색인,트리거등이 저장
# 용량이 작아 메모리에 올리기도 쉽고 속도도 빠른편
# 안드로이드, ios에는 기본적으로 포함되어 있음
# 단, 복잡하고 용량이 큰 데이터를 저장하기에는 다소 적절치 않음
# sqlite.org

import sqlite3

# 회원정보를 입력받아 member 테이블에 저장
# 저장대상 : 아이디, 비밀번호, 이름, 이메일

# 파이썬으로 데이터베이스 다루기 1 - 테이블 생성
# 1. 데이터베이스 연결
conn = sqlite3.connect('db/python.db')

# 2. 데이터베이스 커서 생성
cursor = conn.cursor()

# 3. 실행할 sql 작성
sql = '''create table member(
userid varchar(18) not null,
passwd varchar(18) not null,
name   varchar(10) not null,
email  varchar(35) not null)'''

# 4. 작성한 sql을 실행
cursor.execute(sql)
conn.commit()

# 5. 작업 마무리
cursor.close()
conn.close()

# 파이썬으로 데이터베이스 다루기 2 - 데이터 추가

import sqlite3

# 0

userid = input('아이디를 입력하세요 : ')
passwd = input('비밀번호를 입력하세요 : ')
name = input('이름을 입력하세요 : ')
email = input('이메일을 입력하세요 : ')

# 1
conn = sqlite3.connect('db/python.db')

# 2
cursor = conn.cursor()

# 3
# 비추 - SQL injection 공격 위험 존재
sql = f'''insert into member 
values ('{userid}', '{passwd}', '{name}', '{email}')'''

# 매개변수 placeholder(?)를 이용해서 실제값을 대입
sql = 'insert into member values (?,?,?,?)'
params = (userid,passwd,name,email)

# 4
# cursor.execute(sql)
cursor.execute(sql,params)
print(cursor.rowcount, '건의 데이터가 추가됨!')
conn.commit()

# 5
cursor.close()
conn.close()

# 파이썬으로 데이터베이스 다루기 3 - 데이터 조회

import sqlite3

# 1
conn = sqlite3.connect('db/python.db')

# 2
cursor = conn.cursor()

# 3
sql = 'select * from member'

# 4 sql을 실행하고 결과 집합을 가져옴
cursor.execute(sql)
rs = cursor.fetchall()

# 5 결과집합에서 레코드 단위로 읽어와서 회원정보 출력
result = ''
for r in rs:
    result += f'{r[0]}, {r[1]}, {r[2]}, {[3]}\n'
print(result)

# 6
cursor.close()
conn.close()