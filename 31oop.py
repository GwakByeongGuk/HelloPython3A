# oop : object oriented programming
# 프로그램을 명령어들의 단순 묶음이라고 보는 시각에서
# 벗어나 독립된 객체들의 모음이라고 보는 시각에 근거하여
# 프로그래밍하는 패러다임

# 프로그램을 보다 유연하게 작성할 수 있고
# 코드의 재사용을 높일 수 있으며
# 대규모 소프트웨어 개발 시 유지보수가 용이함

# 프로그램의 각 구성요소를 실제세계의


# ex) 성적처리 프로그램
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 출력

# 성적 입력
name = input('이름은 ?')
kor = int(input('국어는 ?'))
eng = int(input('영어는 ?'))
mat = int(input('수학은 ?'))

# 성적 처리
tot = kor + eng + mat
avg = tot / 3
grd = '가'
if (avg >= 90): grd = '수'
elif (avg >= 80): grd = '우'
elif (avg >= 70): grd = '미'
elif (avg >= 60): grd = '양'

# 결과 출력
print(f'입력: {name}, {kor}, {eng}, {mat}')
print(f'결과: {tot}, {avg:.1f}, {grd}')

# ex) 성적처리 프로그램 2
# 함수 기반 : 처리코드들을 기능별로 하나의 이름으로 묶음
def readSungJuk():
    name = input('이름은 ?')
    kor = int(input('국어는 ?'))
    eng = int(input('영어는 ?'))
    mat = int(input('수학은 ?'))
    return name,kor,eng,mat

# 성적 처리
def computeSungJuk(kor,eng,mat):
    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if (avg >= 90): grd = '수'
    elif (avg >= 80): grd = '우'
    elif (avg >= 70): grd = '미'
    elif (avg >= 60): grd = '양'
    return tot,avg,grd

# 결과 출력
def printSungJuk(name,kor,eng,mat,tot,avg,grd):
    print(f'입력: {name}, {kor}, {eng}, {mat}')
    print(f'결과: {tot}, {avg:.1f}, {grd}')

# 프로그램 실행
name,kor,eng,mat = readSungJuk()
tot,avg,grd = computeSungJuk(kor, eng, mat)
printSungJuk(name, kor, eng, mat, tot, avg, grd)

# ex) 성적처리 프로그램 3
# 객체지향 프로그램 : 기능을 구현하는데 사용된 함수들과 관련된 변수들을 하나로 묶음
# 단, 성적데이터를 담고있는 객체와,
# 성적처리에 필요한 기능들로 구성된 객체등으로 나눠 작성

# OOP에서 클래스의 종류
# 1. 값만 저장하는 클래스 : VO, DTO
# 2. 기능만 저장하는 클래스 : Service (SO), DAO
# 3. UI만 저장하는 클래스 : UO

# 클래스 정의
# class 클래스명(상속여부):
#     생성자
#     setter/getter
#     매서드

# 1. 값만 저장하는 클래스 : VO
# 생성자 : __init__ (매직함수)
# 클래스내에 선언된 변수 - 멤버변수 (주로 private 접근제한자 사용)

class SungJuk():
    # 생성자 :
    # 변수선언 :
    def __init__(self):
        self.name = '홍길동'
        self.kor = 0
        self.eng = 0
        self.mat = 0
        self.tot = 0
        self.avg = 0.0
        self.gnd = 0

# 성적 객체 생성
# 클래스를 이용해서 메모리 상에 변수를 만듦
# 변수명 = 클래스명()
sj = SungJuk()

# 객체의 멤버변수 접근 : 객체명, 멤버변수명
print(sj.name)
print(sj.kor, sj.eng, sj.mat)

# 사원 데이터를 클래스(Employee)로 정의

class Employee():
    def __init__(self):
        self.empid = 100
        self.fname = 'Steven'
        self.lname = 'King'
        self.email = 'SKING'
        self.phone = '515.123.4567'
        self.hdate = '2003-06-17'
        self.jobid = 'AD_PRES'
        self.sal = 24000
        self.comm = None
        self.mgrid = None
        self.deptid = 90

emp = Employee()
print(emp.empid, emp.fname, emp.lname)

# 성적 데이터를 클래스로 다루기
sj = SungJuk()

sj.name = input('이름은? ')
sj.kor = int(input('국어는? '))
sj.eng = int(input('영어는? '))
sj.mat = int(input('수학은? '))

print(sj.name,sj.kor,sj.eng,sj.mat)

# 개선된 성적 클래스 - 생성자를 통해 객체 초기화
class SungJuk2():
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.avg = 0.0
        self.grd = '가'

    # __str__ : 멤버변수들의 값을 문자열화해서
    # 객체 정보를 외부에 출력할 때 사용하는 특수한 함수
    def __str__(self):
        result = f'{self.name} {self.kor} {self.eng} {self.mat}'
        return result

# 성적 개체 생성 및 초기화
sj = SungJuk2('',99,98,99)

# 성적 객체 출력
print(sj.name,sj.kor,sj.eng,sj.mat)
print(sj)

# 성적 객체 생성 및 초기화 2
sj = SungJuk2(input('이름은? '), int(input('국어는? ')),
              int(input('영어는? ')), int(input('수학은? ')))
print(sj)

# 2. 기능만 저장하는 클래스 1 - Service
class SungJukService():
    def read_sungjuk(self):
        name = input('이름은? ')
        kor = int(input('국어는? '))
        eng = int(input('영어는? '))
        mat = int(input('수학은? '))
        return SungJuk2(name,kor,eng,mat)

    def compute_sungjuk(self,sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '수' if sj.avg >= 90 else \
            '우' if sj.avg >= 80 else \
                '미' if sj.avg >= 70 else \
                    '양' if sj.avg >= 60 else '가'

sjsrv = SungJukService()
sj = sjsrv.read_sungjuk()
sjsrv.compute_sungjuk(sj)

print(sj)
print(sj.tot,sj.avg,sj.grd)

# 3. 기능만 저장하는 클래스 2 - DAO
class SungJukDAO:
    def insertSungJuk(self,sj):
        pass
    def selectSungJuk(self):
        pass
    def selcetOneSungJuk(self,sjno):
        pass
    def updateSungJuk(self,sj):
        pass
    def deleteSungJuk(self,sjno):
        pass

sjdao = SungJukDAO()
sjdao.insertSungJuk(sj)
sjdao.selectSungJuk()