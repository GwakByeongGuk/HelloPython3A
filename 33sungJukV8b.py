# 성적 처리 프로그램 v8
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로 재작성
# 즉, 성적 입력, 조회, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생 성적 데이터는 sungjuk 테이블에 저장
# 클래스 기반으로 프로그램 재작성
# mariadb 10.6 기반

import sys
from teereal.oop.services import SungJukService as sjv8


# 메뉴 출력 및 메뉴별 처리
while True:
    # 메뉴 입력받음
    menu = sjv8.display_menu()

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('성적 데이터 추가')
        sjv8.add_sungjuk()

    elif menu == '2':
        print('성적 데이터 조회')
        sjv8.show_sungjuk()

    elif menu == '3':
        print('성적 데이터 상세조회')
        sjv8.showone_sungjuk()

    elif menu == '4':
        print('성적 데이터 수정')
        sjv8.modify_sungjuk()

    elif menu == '5':
        print('성적 데이터 삭제')
        sjv8.remove_sungjuk()

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다!!')