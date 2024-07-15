# 반복문
# 특정 문장/코드를 지정할 횟수/조건에 반복 실행하는 문장

# 간단한 메세지 한번 출력
print('Hello, Python!')

# 간단한 메세지 여러번 출력
print('Hello, Python!')
print('Hello, Python!')
print('Hello, Python!')

# 메세지를 수정한다면? - 번거로움!
print('Hello, Cloud!')
print('Hello, Cloud!')
print('Hello, Cloud!')

# 만약, 반복문을 사용한다면?
# 반복의 용이성과 수정의 편리함을 제공

# 파이썬의 반복문
# for : 지정한 횟수만큼 반복 수행
# while : 지정한 조건에 의해 반복 수행

# 횟수에 따른 반복 - for
# 반복횟수는 range() 함수로 유추가능

# for 카운트변수 in range(시작값, 종료값 -1, 간격):
#     반복할 문장

# range 함수
# 시작값과 종료값-1 사이의 연속된 정수를 반환
print(1,2,3,4,5,6,7,8,9,10)

print(list(range(1,11)))
print(list(range(1,11,2)))

# for 사용예
#for i in [1,2,3,4,5,6,7,8,9,10]:
for i in range(1,10+1): # start ~ end -1
    print(i)

for i in range(3): # 0 ~ end-1
    print(f'Hello, World!! {i}')

for _ in range(3): # 카운트변수 생략
    print(f'Hello, World!!')

# 1 ~ 100 사이 모든 정수의 합을 구하시오
sum = 0
for i in range(1,101):
    sum += i
print(sum)

# 1 ~ 100 사이 짝수의 합을 구하시오

sum = 0
for i in range(2,101,2):
    sum += i
print(sum)

# 메일 발송
count = int(input('메일 발송 횟수를 입력하세요 : '))

for _ in range(count):
    print('메일발송!')

# 3의 배수 출력하기
result = ''

for i in range(1, 10+1):
    result += f'num = {i}\n'
    if i % 3 == 0:
        result += f'3의배수!!\n'

print(result)

# 구구단 출력하기(5단)
result = ''
dan = 5
for i in range(1, 11):
    result += f'{dan} x {i} = {dan * i}\n'

print(result)

# 줄바꿈 없이 출력하기 (end='')
result = ''
for i in range(1, 10+1):
    # print(i, end='/')
    result += f'{i}'

print(result)

# 3과 7의 공배수
result = ''
for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        result += f'{i} '

print(result, f'[{3 * 7}]')


# range함수 사용예
print(list(range(-10, 0, 1)))
print(list(range(10, 0, -1)))

# 문자열을 for문 사용하기
# str = 'Hello, World!!'
#
# for c in str:
#    print(c, end=' ')
# -----------------------------------------
# 369 게임
# 1 ~ 10 : 3, 6, 9
# 11 ~ 20: 13, 16, 19
# ...
# 31 ~ 39 : 31, 33, 36, 39

# 369 게임: 1부터 100까지
def play_369_game():
    result = []
    for i in range(1, 101):
        count = 0
        num = i
        while num > 0:
            digit = num % 10
            if digit in (3, 6, 9):
                count += 1
            num //= 10

        if count > 0:
            result.append(f'{i} ' + '짝!' * count)

    return result

# 결과 출력
for line in play_369_game():
    print(line)

# ---------------------------------------------------------

for i in range(1, 101):
    if i < 10:
        if i % 3 == 0:
            print(f'{i} 짝!')
        else:
            print(i)
    else:
        clap = ''

        fnum = i // 10
        lnum = i % 10

        if fnum % 3 == 0:clap += '짝!'
        if lnum % 3 == 0 and lnum != 0:clap += '짝!'

        print(f'{i} {clap}')


# 열차 교차 시간 알아내기
# 오전 9시 - 오후 6시
trainA = 10
trainB = 25
trainC = 30

for min in range (1,540+1):
    if min % trainA == 0 and min % trainB == 0:
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : A - B 교차!')
    elif min % trainB == 0 and min % trainC == 0:
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : B - C 교차!')
    elif min % trainA == 0 and min % trainC == 0:
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : A - C 교차!')

# 로그인 기능 만들기
isLogin = False
for i in range(5):
    if not isLogin:
        passwd = input('관리자 암호를 입력하세요. ')
        if passwd == 'hanbitac':
            isLogin = True
            print('로그인 되었습니다.')
            break
        else:
            print('암호를 다시 입력하세요!')

if not isLogin:
    print('로그인 실패!! 횟수 초과!!!')