# 성적 DAO 클래스
import pymysql

from teereal.oop.models import SungJuk

class SungJukDAO:
    # 데이터베이스 연결 문자열
    host = '3.35.133.116'
    dbname = 'clouds2024'
    user = 'clouds2024'
    passwd = 'clouds2024'

    # 데이터베이스 객체와 커서 생성
    @staticmethod
    def _make_conn():
        conn = pymysql.connect(host=SungJukDAO.host, user=SungJukDAO.user,
                               password=SungJukDAO.passwd, database=SungJukDAO.dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 객체와 커서 생성
    @staticmethod
    def _dis_conn(conn,cursor):
        cursor.close()
        conn.close()

    @staticmethod
    def insert_sungjuk(sj):
        """
        입력한 성적데이터를 sungjuk 테이블에 저장
        :param sj: 테이블에 저장할 성적데이터
        :return cnt: 테이블에 성공적으로 저장된 데이터 건수
        """
        sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd) \
               values (%s,%s,%s,%s, %s,%s,%s)'
        conn,cursor = SungJukDAO._make_conn()
        params = (sj.name,sj.kor,sj.eng,sj.mat,sj.tot,sj.avg,sj.grd)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn,cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        """
        sungjuk 테이블에서 모든 성적 데이터(번호/이름/국어/영어/수학/등록일)를 읽어옴
        :return: 조회된 성적데이터 객체
        """
        sjs = []
        sql = 'select sjno,name,kor,eng,mat,substr(regdate,0,11) from sungjuk'
        conn,cursor = SungJukDAO._make_conn()
        cursor.execute(sql)
        rs = cursor.fetchall()
        for r in rs:
            sj = SungJuk(r[1],r[2],r[3],r[4])
            sj.sjno = r[0]
            sj.regdate = r[5]
            sjs.append(sj)
        SungJukDAO._dis_conn(conn,cursor)
        return sjs

    @staticmethod
    def selectone_sungjuk(sjno):
        """
        sungjuk 테이블에서 특정 학생의 성적데이터를 읽어옴
        :param sjno: 조회할 학생 번호
        :return: 조회된 성적데이터 객체
        """
        sql = 'select * from sungjuk where sjno = %s'
        conn,cursor = SungJukDAO._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        rs = cursor.fetchone()
        if rs:
            sj = SungJuk(rs[1],rs[2],rs[3],rs[4])
            sj.sjno = rs[0]
            sj.tot = rs[5]
            sj.avg = rs[6]
            sj.grd = rs[7]
            sj.regdate = rs[8]
        else:
            sj = None
        SungJukDAO._dis_conn(conn,cursor)
        return sj

    @staticmethod
    def update_sungjuk(sj):
        """
        기존에 있던 성적데이터를 새로 입력한 성적데이터로 바꿔 테이블에 저장
        :param sj:
        :return:
        """
        sql = 'update sungjuk set kor=?, eng=?, mat=?, tot=?, avg=?, grd=? \
           where sjno=?'
        conn,cursor = SungJukDAO._make_conn()
        params = (sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sj.sjno)
        cursor.execute(sql, params)
        print(cursor.rowcount, '건의 데이터 수정됨!')
        conn.commit()
        cnt = cursor.rowcount
        SungJukDAO._dis_conn(conn,cursor)
        conn.close()
        return cnt


    @staticmethod
    def delete_sungjuk(sjno):
        conn,cursor = SungJukDAO._make_conn()
        sql = ('delete from sungjuk where sjno = ?')
        params = (sjno,)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn,cursor)
        return cnt