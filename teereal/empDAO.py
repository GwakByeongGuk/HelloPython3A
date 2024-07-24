import pymysql

class empDAO:
    # 데이터베이스 연결 문자열
    host = '3.35.133.116'
    dbname = 'clouds2024'
    user = 'clouds2024'
    passwd = 'clouds2024'

    @staticmethod
    def _make_conn():
        conn = pymysql.connect(host=empDAO.host, user=empDAO.user,
                               password=empDAO.passwd, database=empDAO.dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 객체와 커서 생성
    @staticmethod
    def _dis_conn(conn,cursor):
        cursor.close()
        conn.close()

    # 사원 데이터 총 갯수 조회
    @staticmethod
    def getTotalEmp():
        sql = 'select count(empid) + 1 total from emp'
        conn,cursor = empDAO._make_conn()
        cursor.execute(sql)
        rs = cursor.fetchone()
        cnt = rs[0]
        empDAO._dis_conn(conn,cursor)
        return cnt

    # 처리된 사원데이터를 테이블에 저장
    @staticmethod
    def newEmp(emp):
        sql = '''insert into emp (empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)
             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        conn, cursor = empDAO._make_conn()
        params = (emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7], emp[8], emp[9], emp[10])
        cursor.execute(sql, params)
        conn.commit()
        empDAO._dis_conn(conn, cursor)



    # 사원 데이터 전체 조회
    @staticmethod
    def readAllEmp():
        sql = 'select empid,fname,lname,email,jobid,deptid from emp'
        conn,cursor = empDAO._make_conn()
        cursor.execute(sql)
        sjs = cursor.fetchall()
        empDAO._dis_conn(conn,cursor)
        return sjs

    # 학생 한명의 성적 상세 조회
    @staticmethod
    def readOneEmp(empid):
        sql = 'select * from emp where empid = %s'
        conn,cursor = empDAO._make_conn()
        params = (empid,)
        cursor.execute(sql, params)
        emp = cursor.fetchone()
        empDAO._dis_conn(conn,cursor)
        return emp

    @staticmethod
    def deleteEmp(empid):
        conn,cursor = empDAO._make_conn()
        sql = 'delete from emp where empid = %s'
        params = (empid,)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        empDAO._dis_conn(conn,cursor)
        return cnt

    @staticmethod
    def modifyEmp(emp):
        sql = '''update emp set email=%s, phone=%s, jobid=%s, sal=%s, comm=%s, mgrid=%s, deptid=%s
                 where empid=%s'''
        conn,cursor = empDAO._make_conn()
        params = (emp[3],emp[4],emp[6], emp[7],emp[8],emp[9],emp[10])
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        empDAO._dis_conn(conn,cursor)
        return cnt

    @staticmethod
    def updateEmp(emp):
        return 0

