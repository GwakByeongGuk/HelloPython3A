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
i = 0
while i < 100:
    i += 1
    if i % 3 == 0 and i % 8 == 0:
        print(i)

# 삼각형 넓이 계산하기
i = 1 # 밑변 1부터 2의 배수로 증가
j = 1 # 높이 1부터 3의 배수로 증가
k = 0 # 넓이
while k < 150:
    i += 2
    j += 3
    k = i*j/2
    if k > 150:
        break
    print(k)


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


