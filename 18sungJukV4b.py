# 성적 처리 프로그램 v3b
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적 처리 프로그램으로 재작성
# 즉, 성적 입력, 조회, 상세 조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 규횐 - 기능별 메뉴 선택 시 해당 명령 수행
# 학생 성적 데이터는 개별 변수가 아닌 리스트 안에 dict 형태로 저장

# 프로그램 메뉴 정의

import sys

sjs = []  # 성적 데이터 리스트

main_menu = '''
=========================
     성적 프로그램 V4b
=========================
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 성적 데이터 종료
=========================    
'''

for i in range(100):
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')

    if menu == '1':
        print('성적 데이터 추가')
        sj = {}
        sj['name'] = input("학생 이름: ")
        sj['kor'] = int(input("국어 점수: "))
        sj['eng'] = int(input("영어 점수: "))
        sj['mat'] = int(input("수학 점수: "))
        sj['tot'] = sj['kor'] + sj['eng'] + sj['mat']
        sj['avg'] = sj['tot'] / 3
        sj['grd'] = '수' if sj['avg'] >= 90 else '우' if sj['avg'] >= 80 else \
            '미' if sj['avg'] >= 70 else '양' if sj['avg'] >= 60 else '가'
        sjs.append(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        for sj in sjs:
            print(f'이름 : {sj["name"]}, 국어 : {sj["kor"]}, 영어 : {sj["eng"]}, 수학 : {sj["mat"]}')

    elif menu == '3':
        print('성적 데이터 상세조회')
        for sj in sjs:
            print(f'이름 : {sj["name"]}, 국어 : {sj["kor"]}, 영어 : {sj["eng"]}, 수학 : {sj["mat"]}, '
                  f'총합 : {sj["tot"]}, 평균 : {round(sj["avg"],1)}, 학점 : {sj["grd"]}')

    elif menu == '4':
        print('성적 데이터 수정')
        name = input('수정할 학생의 이름을 입력하세요: ')
        for sj in sjs:
            if sj['name'] == name:
                print(f'기존 성적: 국어: {sj["kor"]}, 영어: {sj["eng"]}, 수학: {sj["mat"]}')
                sj['kor'] = int(input(f'{name}의 새로운 국어 점수: '))
                sj['eng'] = int(input(f'{name}의 새로운 영어 점수: '))
                sj['mat'] = int(input(f'{name}의 새로운 수학 점수: '))
                sj['tot'] = sj['kor'] + sj['eng'] + sj['mat']
                sj['avg'] = sj['tot'] / 3
                sj['grd'] = '수' if sj['avg'] >= 90 else '우' if sj['avg'] >= 80 else \
                    '미' if sj['avg'] >= 70 else '양' if sj['avg'] >= 60 else '가'
                break

    elif menu == '5':
        print('성적 데이터 삭제')

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다!!')
