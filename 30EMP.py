# 사원 등록 프로그램

import sys
import teereal.emp as emp


# 메뉴 출력 및 메뉴별 처리
while True:
    # 메뉴 입력받음
    menu = emp.displayMenu()

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('사원 데이터 추가')
        emp.addEmp(emp)

    elif menu == '2':
        print('사원 데이터 조회')
        emp.showEmp()

    elif menu == '3':
        print('사원 데이터 상세조회')
        emp.showOneEmp()

    elif menu == '4':
        print('사원 데이터 수정')
        emp.modifyEmp(emp)
    elif menu == '5':
        print('사원 데이터 삭제')
        emp.deleteEmp()
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')