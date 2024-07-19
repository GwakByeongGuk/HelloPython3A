# 프로그램 메뉴 정의
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적 처리 프로그램으로 재작성
# 즉, 성적 입력, 조회, 상세 조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생 성적 데이터는 개별 변수가 아닌 리스트 안에 리스트 형태로 저장
# 리스트 형태로 저장된 성적 데이터는 csv형식을 변환해서
# sungjuk.dat에 저장해 둠

import csv

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
sjs = []


# 성적 데이터 받는 변수
def readSungJuk():
    sj = []
    cnt = len(sjs) + 1
    sj.append (input(f'{cnt}번학생 이름을 입력하시오: '))
    sj.append(int(input(f'{cnt}번 학생 국어 성적을 입력하시오: ')))
    sj.append(int(input(f'{cnt}번 학생 영어 성적을 입력하시오: ')))
    sj.append(int(input(f'{cnt}번 학생 수학 성적을 입력하시오: ')))
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(round(sj[4] / 3,1))
    grd = '수' if sj[5] >= 90 else '우' if sj[5] >= 80 else '미' if sj[5] >= 70 else '양' if sj[5] >= 60 else '가'
    sj.append(grd)
    return sj

# 입력받은 성적 데이터를 처리하고 리스트에 저장
def addSungJuk():
    sj = readSungJuk()
    if len(sj) == 7:
        sjs.append(sj)
        saveSungJuk()

# 리스트에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    for sj in sjs:
        result += f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}, 총점: {sj[4]}, 평균: {sj[5]}, 등급: {sj[6]}\n'
    print(result)

# sungjuk.dat에 저장된 성적데이터를 읽어서
# sjs 변수에 초기화
def loadSungJuk():
    with open('c:/Users/cloud6a/Documents/Projects2024/HelloPythonA/teereal/sungjuk.dat', 'r', encoding='UTF-8') as f:
        rows = f.readlines()

        for row in rows:
            data = row.split(',')
            sj = [d for d in data]
            sjs.append(sj)


# 메모리에 생성된 sjs변수의 모든 데이터를
# sungjuk.dat에 저장
def saveSungJuk():
    data = ''
    for sj in sjs:
        data += f'{sj[0]},{sj[1]},{sj[2]},{sj[3]},{sj[4]},{sj[5]},{sj[6]}\n'

    with open('c:/Users/cloud6a/Documents/Projects2024/HelloPythonA/teereal/sungjuk.dat', 'w', encoding='UTF-8') as f:
        f.write(data)

def main():
    loadSungJuk()
    while True:
        menu = displayMenu()
        if menu == '1':
            addSungJuk()
        elif menu == '2':
            showSungJuk()
        elif menu == '0':
            saveSungJuk()
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")
if __name__ == "__main__":
    main()