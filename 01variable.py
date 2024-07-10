# 변수 variable
# 어떤 값을 저장하는 장소(메모리)를 기억하기 쉽게 문자로 나타낸 것
# 변수에 값이 저장되는 공간은 메모리라고 함
# 변수에 값을 넣어라고 선언하면,
# 시스템상의 메모리 어딘가에 공간을 확보하고
# 그 공간의 실제주소와 이름을 연관mapping함

# 변수 선언, 초기화


# 이름과 나이를 저장하는 변수 선언
# 변수명 = 값
a = '홍길동'
b = 99

name = '홍길동'  # 의미있는 단어로 변수 선언
age = 99

Name = '일지매'  # 변수명은 대소문자 구분

# 변수에 저장된 값을 출력하려면 print 함수 사용
# print(변수명, 변수명, ...)
print(name, age)

# 변수 선언 후 값 변경
intro = 'Hello, Python'
print(intro)

intro = '안녕하세요, 파이썬'
print(intro)

# 변수명 작성 규칙

# 파이썬 예약어
import keyword
print(keyword.kwlist)


# 자료형 datatype
# 정적static 자료형
# 변수선언시 자료형도 함께 지정
# 변수의 자료형은 컴파일 시간에 결정 - 오류발생 적음
# String name = '홍길동'
#        name = 123 (오류발생!-선언시 자료형과 대입시 값의 자료형이 다름)

# 동적dynamic 자료형
# 변수선언시 자료형은 생략가능, 추론기능으로 자동할당
# 변수의 자료형은 실행 시간에 결정 - 오류발생 여지 존재
# 변수에 대입하는 값에 따라 자료형이 바뀔수도 있음
# name = '홍길동'
# name = 123   (문제없음!-변수의 자료형은 자동으로 바뀜)

# ex) 회원정보 저장용 변수 선언
# 아이디, 비번, 이름, 나이, 이메일,
# 결혼여부, 보유금액, 등록일
userid = 'abc123'
passwd = '987xyz'
name = '홍길동'
age = 99
email = 'abc123@987xyz.co.kr'
married = True
money = 10000
regdate = '2024-07-09 12:15:35'


# 파이썬에서 제공하는 자료형 - 정수, 실수, 문자, 블리언boolean
# primitive data type - 메모리에 데이터(값) 그 자체를 저장

# 문자형
# 파이썬에서 문자char와 문자열string을 문자형으로 취급
# 문자형은 ''나 ""를 이용해서 정의 - ''를 추천!
# 여러줄 문자열text을 작성할때는 ''' '''를 사용
# 긴 문장은 \로 나눠 작성 가능
str1 = 'Hello, World!!'
str2 = "Hello, World!!"

str3 = "insert into member \
values ('','','')"

str4 = "Hello, \nWorld!!"
str5 = '''Hello,
World!!'''
print(str1, str2, str3, str4, str5)

# 정수형 - 소수점이하 값이 없는 숫자
int1 = 123
int2 = 1234561234567  # 큰 정수도 표현가능
int3 = 0b00001000   # 2진수 : 0b~
int4 = 0x000FFFF   # 16진수 : 0x~

print(int1, int2, int3, int4, hex(65535), bin(65535))

# 실수형 - 소수점이하 값이 있는 숫자
# 부동소수점floating point 실수 : 국제표준에 따라 실수를 표기하는 방식
# 즉, 실수를 정수부와 정수의 곱으로 된 지수로 표현하는 것
# 123.456 -> 123456 x 10^-3
# 단, 파이썬에서는 유효숫자 e지수를 이용해서 지수부를 표현
# 123.456 -> 123456 x e-3

float1 = 3.141213
float2 = 123.456
float3 = 123456e-3

print(float1, float2, float3)

# 부동소수점과 오차
# 컴퓨터에서 숫자는 2진수 기반으로 표현하기 때문에
# 실수는 정확하게 나타내기 어려움! - 단지, 근사값으로만 표현
# 0.1 + 0.2 == 0.3

print(0.1 + 0.2, 0.3)
print(round(0.1 + 0.2, 5), round(0.3, 5))

# 논리형
# 논리적인 값을 표현할때 사용 - 참True(1), 거짓False(0)
# 논리연산(조건식), 조건문, 상태를 표시하는 플래그변수
bool1 = True
bool2 = False

print(bool1, bool2, bool1 == 1, bool2 == 0)

# 리터럴

# type 함수 : 리터럴이나 변수의 자료형 출력
print(type(str1), type(int1), type(float1), type(bool1))
print(type('Hello'), type(123), type(3.14), type(True))

# 자료형 변환(type conversion/casting)
# 어떤 자료형에거 다른 자료형으로 변환하는 것
# 암시적implicit 변환 - 자동으로 컴파일러가 변환
# 명시적explicit 변환 - 개발자가 직접 변환 (int, str, float, bool)

result1 = 5 + 3.14152   # 정수 + 실수
print(result1, type(result1))

result2 = True + 1     # 블리언 + 정수
print(result2, type(result2))

result3 = 3 == 4       # 정수끼리 비교
print(result3, type(result3))

print(type(int1), str(int1), type(str(int1)))

# print(type(str1), int(str1)) # 실행불가!

str6 = '3.14152'
# print(type(str6), int(str6), type(int(str6))) # 실행불가
print(type(str6), float(str6), type(float(str6)))

print(bool(''), bool('abc123'))  # 문자를 bool로 변환시

# 사용자로부터 값을 입력받아 변수 초기화
# 변수명 = input(메세지)
# 주의! - input함수로 입력받은 값은 무조건 문자로 취급

# 이름과 나이를 입력받아 출력
name = input('이름은? ')
age = input('나이는? ')

print(name, age)

# 환율 계산프로그램 작성
# 달러를 입력하면 원화로 계산해서 출력 (1$ -> 1382.12원)
dollar = input('달러는? ')
won = int(dollar) * 1382.12
print(dollar, won)


# 문자열 템플릿
# 파이썬에서 문자열 속에 변수를 포함시켜 출력할때 유용하게 사용하는 방법
# f-string : python 3.6부터 도입, f'문자열 {변수명:포맷팅}'

lang = 'Python'
print('Hello,', lang, '!!')
print(f'Hello, {lang} !!')

riseSun = '오전 6시 30분'
downSun = '오후 7시 20분'

print(f'일출시간은 {riseSun}이고, 일몰시간은 {downSun}입니다.')
