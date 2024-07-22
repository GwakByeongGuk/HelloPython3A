import sqlite3

def displayMenu():
    main_menu = '''
    ========================
        사원 데이터 CRUD
    ========================
        1. 사원 데이터 추가
        2. 사원 데이터 조회
        3. 사원 데이터 상세조회
        4. 사원 데이터 수정
        5. 사원 데이터 삭제
        0. 사원 데이터 종료
    ========================
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

def readEMPData():
    emps = []
    emps.append(int(input('사원 번호를 입력하시오: ')))
    emps.append(input('사원 퍼스트네임을 입력하시오: '))
    emps.append(input('사원 라스트네임을 입력하시오: '))
    emps.append(input('사원 이메일을 입력하시오: '))
    emps.append(input('사원 전화번호를 입력하시오: '))
    emps.append(input('사원 고용일을 입력하시오: '))
    emps.append(input('사원 직책을 입력하시오: '))
    emps.append(float(input('사원 연봉을 입력하시오: ')))
    emps.append(float(input('사원 커미션을 입력하시오: ')))
    emps.append(int(input('사원 상사 번호를 입력하시오: ')))
    emps.append(int(input('사원 부서 번호를 입력하시오: ')))
    return tuple(emps)

def addEMPData():
    emps = readEMPData()
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    sql = ('INSERT INTO HR (empid,fname,lname,email,phone,hdate,jobid,'
           'sal,comm,mgrid,deptid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)')
    cursor.execute(sql, emps)
    conn.commit()
    cursor.close()
    conn.close()
    print("사원 데이터가 추가되었습니다.")

def showEMPData():
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    sql = 'SELECT empid,fname,lname,email,jobid,deptid FROM HR'
    cursor.execute(sql)
    rows = cursor.fetchall()
    result = ''
    for row in rows:
        result += f'사원번호: {row[0]}, 이름: {row[1]} {row[2]}, 이메일: {row[3]}, 직책: {row[4]}, 부서번호: {row[5]}\n'
    cursor.close()
    conn.close()
    print(result)

def showDetailEMPData():
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    sql = 'SELECT * FROM HR'
    cursor.execute(sql)
    rows = cursor.fetchall()
    result = ''
    for row in rows:
        result += (f'사원번호: {row[0]}, 이름: {row[1]} {row[2]}, 이메일: {row[3]}, 전화번호: {row[4]}, '
                   f'고용일: {row[5]}, 직책: {row[6]}, 연봉: {row[7]}, 커미션: {row[8]}, '
                   f'상사번호: {row[9]}, 부서번호: {row[10]}\n')
    cursor.close()
    conn.close()
    print(result)

def creatTable():
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS HR')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HR (
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
    )
    ''')

def loadEMPData():
    with open('c:/Users/cloud6a/Documents/Projects2024/HelloPythonA/teereal/HR.dat', 'r', encoding='UTF-8') as f:
        rows = f.readlines()
        for row in rows:
            data = row.split(',')
            emps = [d for d in data]
            data.append(emps)

def main():
    loadEMPData()
    while True:
        menu = displayMenu()
        if menu == '1':
            addEMPData()
        elif menu == '2':
            showEMPData()
        elif menu == '3':
            showDetailEMPData()
        elif menu == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()


