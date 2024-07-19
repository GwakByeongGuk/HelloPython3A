# 매개변수parameter
# 함수 정의 부분에서 괄호안에 선언된 변수를 의미
# 함수 호출할떄, 이 매개변수에 값을 전달하면
# 함수내에서 해당 값을 사용할 수 있음
# 즉, 매개변수는 함수에 입력된 데이터를 제공하는 역할 담당
# 한편, 인수는 함수 호출시 함수에 전달하는 실제 값을 의미
# 즉, 함수 호출시 괄호안에 넣은 값을 의미
# 이 값은 함수의 매개변수를 할당되어 사용

# 가변인수
# 함수 호출시 인수의 갯수가 가변적일 수 있게 하는 기능
# 이를 통해 필요한 만큼의 인수를 자유롭게 전달 가능
# 파이썬에서는 *args, **kwargs라는 구문 사용
# 단, *args -> 튜플, **kwargs -> dict 형태로 전달됨

def print_args(*args):
    print(args)

print_args(1, 2, 3)
print_args('a', 'b', 'c', 'd', 'e')

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b=2, c=3)
print_kwargs(name='일지매', kor=99, eng=98, mat=99)

# 언패킹
# 시퀀스 자료형이나 dict 등의 값을 개별변수에 할당하는 과정
# 이것을 이용해서 컨테이너 자료형의 값들을 효율적으로 다룰 수 있음

# 리스트 언패킹
a, b, c = [1, 2, 3]
print(a, b, c)

x, y, z = 'xyz'
print(x, y, z)

# dict 언패킹
member = {'userid': 'abc123', 'passwd': '987xyz'}

uid, pwd = member.values()
print(uid, pwd)

uid, pwd = member.keys()
print(uid, pwd)

uid, pwd = member.items()  # py3.8이상
print(uid, pwd)

# 가변인수 언패킹
# 이전 예 : print_args(1, 2, 3)
mylist = [1, 2, 3]
mydict = {'a':4, 'b':5, 'c':6}
print_args(*mylist)
print_kwargs(**mydict)

def print_args(a, b, c):
    print(a, b, c)

print_args(*mylist)     # 리스트의 값들을 개별적으로 출력
print_args(**mydict)    # dict의 값들을 개별적으로 출력

# 매개변수 기본값
# 함수 정의시 매개변수의 기본값을 지정하면
# 함수 호출시 매개변수에 인수가 할당되지 않을 경우,
# 기본값이 대신 할다왿ㅁ - 함수를 좀 더 유연하게 사용가능

def sayHello(name, say):
    print(f'{name}, {say}')

sayHello('홍길동', '안녕')
sayHello('일지매', '하이')
sayHello('박세리')
sayHello()

# 반환값
# 함수는 작업을 수행한 후 그 결과를 반환할 수 있음
# 이때 반환되는 값을 반환값이라고 함
# 반환값은 함수 내부에서 return이라는 키워드로 지정

# 제곱값을 계산하는 함수
def squr(x):
    # 출력까지 함수에서 구현하기 때문에
    # 플랫폼이 변하는 경우 함수를 재작성해야하는 번거로움 발생!
    print(f'{x}=> {x ** 2}')

squr(2)
squr(10)

# 제곱값을 계산하는 함수2
def squr2(x):
    return x ** 2

print(f'2 => {squr2(2)}')
print(f'10 => {squr2(10)}')

# 함수 실행 중지
# 함수 실행을 중지하고 싶다면 return만 작성
# 즉, return 문 이후의 코드는 실행하지 않음 - 함수 조기 종료 가능

# 제고값을 계산하는 함수3
# 인수가 음수인 경우 함수 실행 중지
def squr3(x):
    if x < 1: return # 음수인 경우 중지
    return x ** 2

squr3(50)
squr3(-1)