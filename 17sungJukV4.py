# 성적 처리 프로그램 v3b
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적 처리 프로그램으로 재작성
# 즉, 성적 입력, 조회, 상세 조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 규횐 - 기능별 메뉴 선택 시 해당 명령 수행
# 학생 성적 데이터는 개별 변수가 아닌 리스트 안에 리스트 형태로 저장

# 프로그램 메뉴 정의

import sys

sjs = []  # 성적 데이터 리스트

main_menu = '''
=========================
     성적 프로그램 V4
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

    # 선택한 메뉴에 따라 해당 기능 수행
    # if menu == '1':
    #     print('성적 데이터 추가')
    #     cnt = len(sjs)
    #     names = input(f"학생 {cnt+1} 이름: ")
    #     kors = int(input(f"{cnt+1}의 국어 점수: "))
    #     engs = int(input(f"{cnt+1}의 영어 점수: "))
    #     mats = int(input(f"{cnt+1}의 수학 점수: "))
    #     tots = kors + engs + mats
    #     avgs = tots / 3
    #     grds = '수' if avgs >= 90 else '우' if avgs >= 80 else \
    #     '미' if avgs >= 70 else '양' if avgs >= 60 else '가'
    #     sjs.append([names, kors, engs, mats, tots, avgs, grds])

    if menu == '1':
        print('성적 데이터 추가')
        sj = []
        cnt = len(sjs)
        sj.append(input(f"학생 {cnt} 이름: "))
        sj.append(int(input(f"{cnt}의 국어 점수: ")))
        sj.append(int(input(f"{cnt}의 영어 점수: ")))
        sj.append(int(input(f"{cnt}의 국어 점수: ")))
        sj.append(sj[1]+sj[2]+sj[3])
        sj.append(sj[4]/3)
        grd = '수' if sj[5] >= 90 else '우' if sj[5] >= 80 else \
            '미' if sj[5] >= 70 else '양' if sj[5] >= 60 else '가'
        sj.append(grd)
        sjs.append(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        for sj in sjs:
            print(f'이름 : {sj[0]}, 국어 : {sj[1]}, 영어 : {sj[2]}, 수학 : {sj[3]}')

    elif menu == '3':
        print('성적 데이터 상세조회')
        for sj in sjs:
            print(f'이름 : {sj[0]}, 국어 : {sj[1]}, 영어 : {sj[2]}, 수학 : {sj[3]}, '
                  f'총합 : {sj[4]}, 평균 : {round(sj[5],1)}, 학점 : {sj[6]}')

    elif menu == '4':
        print('성적 데이터 수정')
        names = input('수정할 학생의 이름을 입력하세요: ')
        for sj in sjs:
            if sj[0] == names:
                print(f'기존 성적 : 국어 : {sj[1]}, 영어 : {sj[2]}, 수학 : {sj[3]} ')
                sj[1] = int(input(f'{names}의 수정할 국어 점수 : '))
                sj[2] = int(input(f'{names}의 수정할 영어 점수 : '))
                sj[3] = int(input(f'{names}의 수정할 수학 점수 : '))
                sj[4] = sj[1] + sj[2] + sj[3]
                sj[5] = sj[4] / 3
                sj[6] = '수' if sj[5] >= 90 else '우' if sj[5] >= 80 else \
                    '미' if sj[5] >= 70 else '양' if sj[5] >= 60 else '가'
                break

    elif menu == '5':
        print('성적 데이터 삭제')

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다!!')
