# 함수
# 특정 기능을 수행하는 코드 블록(모음)에 이름을 부여한 것
# 즉, 여러 곳에 반복적으로 사용할 가치가 있는 코드들을
# 한 뭉치로 묶고 (어떤 값을 입력하면) 결과가 반환되도록
# 작성한 것 - 재사용성이 주 목적
# 이처럼 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악가능
# 다른 사람과의 협업 시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈

print('오늘 날씨는 비옴!') # 단순 출력

print('오늘 날씨는 비옴!') # 반복 출력
print('오늘 날씨는 비옴!')
print('오늘 날씨는 비옴!')

for _ in range(3):      # 개선된 반복
    print('오늘 날씨는 비옴!')

# 만약, 이러한 반복문을 여러번 반복해야 한다면?
# 또, '비옴' 대신 '맑음'이나 '흐림'으로 바꾸고 싶다면?
# => 함수 이용

# 함수 정의
# def 함수명(매개변수):
#       함수몸체

def sayweather():
    for _ in range(3):
        print('오늘 날씨는 비옴!')

# 함수 호출 1
# 함수명()

sayweather()

# 함수 정의 - 매개변수 선언
def say_weather(info):
    for _ in range(3):
        print(f'오늘 날씨는 {info}!')

# 함수 호출 2 - 함수명(인자)
say_weather('비옴')
say_weather('맑음')
say_weather('흐림')

# 단위 변환 : 인치  => 센치미터
def inch_calculation(cm):
    inch = cm / 2.54
    print(f'{cm} cm = {round(inch,4)} inch')
print(inch_calculation(15))

def convert_inch(inch):
    cm = inch * 2.54
    print(f'{inch}  " =>  {cm:.1f} cm')
inch = float(input('길이를 입력하세요. '))
print(inch)

# 변수의 유효범위 scope
# scope : 변수가 접근 가능한 범위를 의미
# 전역 scope : 프로그램의 최상위 레벨에서 정의된 변수
#             어느 곳에서나 접근 가능
#             함수 내에서는 전역변수로의 접근 가능
#             단, 전역변수를 함수 내에서 수정 시
#             global이라는 키워드가 필요
#             사용해서 전역변수에 접근 가능
# 지역 scope : 반복문 내부 / 함수 내부에 정의된 변수
#             반복문이나 함수 내에서만 접근 가능
#             반복문 실행 종료나 함수 호출이 끝나면 자연 소멸

x = 10   # 전역변수
y = 10
def func():
    x = 20
    print('func : x = ', x)

def func2():
    global y
    y = 20
    print('func : y = ', y)

print(x) # x 출력
func()   # x 변수가 있는 함수 호출
print(y)
func2()

# 웹 사이트 방문 누적 횟수 누적 프로그램
visit = 0

isflag = True
while isflag:
    menu = input('1. 웹사이트 방문, 2. 종료 : ')
    if menu == '1':
        visit += 1
        print(f'누적 방문 횟수 : {visit}')
    else:
        print('방문을 종료합니다. ')
        isflag = False

# 누적 방문자 수 처리 함수 정의
def count_visitor():
    global visits
    visits += 1
    print('누적 방문 횟수 : ', visits)

visits = 0

isflag = True
while isflag:
    menu = input('1. 웹사이트 방문, 2. 종료 : ')
    if menu == '1':
        count_visitor()
    else:
        print('방문을 종료합니다. ')
        isflag = False

# ----
goods = 1
goodsCount = [5,2,10,3]

def printReceipt():
    total = 0
    total = 1000 * goodsCount[0] # 리스트는 참조(주소) 자료형이므로
                                 # 별다른 코드 없이 해당 변수 접근가능
    print('total', total)

    goodsCount[0] = 10           # 함수 내에서 global없이 리스트의 일부 변경가능
    total2 = 1000 * goodsCount[0]
    print('total2', total2)

    # goodsCount = [99,99,99,99] # 전역변수 자체를 변경하려고 시도 시
                                 # 오류발생 - global 필요
    print('goodsCount[0]',goodsCount)
    goodsCount[0] = 10
    #print(goods) # goods라는 변수가 선언 안되어 있음
                 # 선언 안된 변수를 호출해서 출력 시도 -실패
    goods = 5    # goods 변수 선언 후 5라는 값 저장 - 성공

printReceipt()
print(goodsCount[0])
print(total)
print(total2)