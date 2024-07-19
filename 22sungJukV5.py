# 프로그램 메뉴 정의

def displayMenu():
    main_menu = '''
    ========================
        성적 프로그램 v5
    ========================
        1. 성적데이터 추가
        2. 성적데이터 조회
        3. 성적데이터 상세조회
        4. 성적데이터 수정
        5. 성적데이터 삭제
        0. 성적데이터 종료
    ========================
    '''
    print(main_menu, end='')
    menu = input('=>메뉴를 선택하세요 : ')
    return menu

# 성적 데이터 관련 변수 선언
sjs = [['일지매', 99, 87, 65, 251, 83.7, '우']]


# 성적 데이터 받는 변수
def readSungJuk():
    sj = []
    cnt = len(sjs)
    sj.append (input(f'{cnt}번학생 이름을 입력하시오: '))
    sj.append(int(input(f'{cnt}번 학생 국어 성적을 입력하시오: ')))
    sj.append(int(input(f'{cnt}번 학생 영어 성적을 입력하시오: ')))
    sj.append(int(input(f'{cnt}번 학생 수학 성적을 입력하시오: ')))
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(sj[4] / 3)
    grd = '수' if sj[5] >= 90 else '우' if sj[5] >= 80 else '미' if sj[5] >= 70 else '양' if sj[5] >= 60 else '가'
    sj.append(grd)
    return sj

# 입력받은 성적 데이터를 처리하고 리스트에 저장
def addSungJuk(sj):
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(sj[4] / 3)
    grd = '수' if sj[5] >= 90 else '우' if sj[5] >= 80 else '미' if sj[5] >= 70 else '양' if sj[5] >= 60 else '가'
    sj.append(grd)
    sjs.append(sj)

# 리스트에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    for sj in sjs:
        result += f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}, 총점: {sj[4]}, 평균: {sj[5]}, 등급: {sj[6]}\n'
    print(result)

