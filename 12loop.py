# while문
# 조건을 만족할 때 까지 반복 수행 - 반복횟수는 모름

# 변수 = 초기값
# while 조건식:
#   반복할 문장:
#   변수증가/감소

# 1 ~ 10 사이 정수 출력
# for i in range (1,11):
#   print(i, end='')
i = 1
while i <= 10:
    print(i, end='')
    i += 1

# 1 ~ 50 사이 정수 중 홀수만 출력
i = 1
while i <= 50:
    print (i, end=' ')
    i += 2

i = 1
while i <= 50:
    if i % 2 != 0:
        print (i, end=' ')
    i += 1

# 1 ~ 50 사이 정수 중 9의 배수만 출력
i = 1
while i <= 50:
    if i % 9 == 0:
        print(i, end= ' ')
    i += 1

# 반복문 내 실행 중지 : break
# for, while문 내에서 반복 흐름을 벗어나기 위해 사용

# 1 ~ 10000 사이 정수의 합을 출력
# 단, 정수의 합이 12345678보다 크면 계산 중지

sum = 0
for i in range(1,10001):
    sum += i
    if sum > 12345678:
        break

i = 0
sum = 0
while i < 10000:
    i += 1
    sum += i
    if sum > 12345678:
        break

# 1 ~ 100 사이의 정수 중
# 3과 8의 공배수만 출력
result = ''
for i in range(1, 100+1):
    if i % 3 == 0 and i % 8 == 0:
        result += f'{i} '

i = 0
while i < 100:
    i += 1
    if i % 3 == 0 and i % 8 == 0:
        print(i)

# 삼각형 넓이 계산하기
limitArea = 150
width = 2
height = 3
i = 1
while True:
    area = ((width * i) * (height * i)) / 2
    if area > limitArea:
        break
    print(f'삼각형의 밑변 : {width*i}cm '
          f'삼각형의 높이 : {height*i}cm '
          f'삼각형의 넓이 : {area}㎠ ')
    i += 1

# 369 게임 (while로 작성)
# '3' in str(36)
# '6' in str(36)
# '9' in str(12)

i = 1
while i < 100:
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i == 33 or i == 66 or i == 99: jjak += ' 짝!'
    print(i, jjak)
    i += 1

# 열차 교차시간 알아보기
trainA = 10
trainB = 25
trainC = 30

start_time = 9
min = 1

while min < 541:
    total_minutes = min
    hour = start_time + min // 60
    minute = total_minutes % 60

    if minute % trainA == 0 and minute % trainB == 0:
        print(f'{hour}시 {minute}분 : A - B 교차!')
    elif minute % trainB == 0 and minute % trainC == 0:
        print(f'{hour}시 {minute}분 : B - C 교차!')
    elif minute % trainA == 0 and minute % trainC == 0:
        print(f'{hour}시 {minute}분 : A - C 교차!')
    min += 1

# 로그인 기능 만들기
cntLogin = 1
while True:
    passwd = input('관리자 암호를 입력하세요: ')

    if passwd == 'hanbitac':
        print('로그인 되었습니다.')
        break
    else:
        print('암호를 다시 입력하세요!')

    if cntLogin < 5:
        cntLogin += 1
    else:
        print('로그인 실패!! 횟수 초과!!!')
        break