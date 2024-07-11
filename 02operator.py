# 수식/표현식 expression
# 숫자, 변수, 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 산술 연산자
# 자료형 승격 promotion

# 매출액 입력 시 총합 출력
num1 = input('1월 매출 :')
num2 = input('2월 매출 :')
num3 = input('3월 매출 :')
totalSale = {int(num1)+int(num2)+int(num3)}
print(f'''
1월 매출 {num1}
2월 매출 {num2}
3월 매출 {num3}
1분기 전체 매출 : {totalSale}원
''')
# 1분기 수익 계산
num1 = input('1분기 매출 :')
num2 = input('1분기 매입 :')
profit = int(num1) - int(num2)
print(f'''
1분기 매출 {num1}
1분기 매입 {num2}
수익 : {profit}원
''')
# 방의 넓이 구하기
num1 = input('가로 :')
num2 = input('세로 :')
area = int(num1)*int(num2)
print(f'''
가로 길이 : {num1}
세로 길이 : {num2}
넓이 : {area} ㎠ 
''')
# 신체질량지수BMI 구하기
num1 = input('몸무게 :')
num2 = input('신장 :')
BMI = float(num1)/(float(num2)**2)
print(f'''
몸무게(kg) : {num1}
신장(m) : {num2}
BMI : {BMI}
''')
# 홀짝 게임
num = input('손 안에 동전 수를 입력하세요. :')
print(f'''
{int(num)%2}
''')
# 빵 나누기
num1 = input('빵의 갯수:')
num2 = input('인당 나누어 줄 빵의 갯수:')
print(f'''
빵을 나누어 줄 수 있는 학생 수 : {int(num1)//int(num2)}
남은 빵 개수 : {int(num1)%int(num2)}
''')
# 전염병 예상 감염자 구하기
num = input('경과 일수:')
print(f'''
{num}일 이후 예상 감염자 수 : {2**int(num)}명
''')

# 할당 연산자 - 어떤 값을 변수에 할당하는 연산자 (=)
# += 더한 뒤 대입, -= 뺀 뒤 대입, *= 곱한 뒤 대입, **= 제곱한 뒤 대입
# /= 나눈 뒤 대입. //= 나눈 뒤 몫을 대입, %= 나눈 뒤 나머지를 대입

# 논리 연산자 단축식 평가
# 논리 연산자 - and, or, not 피연산자의 boolean 값을 기준으로 평가하는 연산자
# 단축 평가란 논리 연산에서 두번째 피연산자를 평가하지 않고 결과를 결정하는 동작
test = 'abcde'
print(('a'and'f')in test) # False
print(('f'and'a')in test) # True

# 삼항 연산자
# 조건문을 한 줄로 표현할 수 있는 연산자
# 참일 때 값 if 조건식 else 거짓일 때 값

myScore = 75
result = '합격!' if myScore >= 90 else '불합격!'
print(result)

# 복리 계산기
money = 5000000
rate = 0.05
money = money + (money * rate) # 1년 후 금액
money = money + (money * rate) # 2년 후 금액
money = money + (money * rate) # 3년 후 금액
money = money + (money * rate) # 4년 후 금액
money = money + (money * rate) # 5년 후 금액

print(f'5년 후 총 수령액 : {int(money):,} 원')

# 범퍼카 탑승
num = int(input('어린이의 신장을 입력하세요 :'))
isRide = (num >= 120)
print(f'{isRide}')
# 범퍼카 탑승 가능 판별
max = 170
min = 120
num = int(input('어린이의 신장을 입력하세요 "'))
print(num >= min & num < max)
# 적자/흑자 판별
num1 = int(input('수입을 입력해주세요 :'))
num2 = int(input('지출을 입력해주세요 :'))
result = '흑자' if (num1 > num2) else '적자'
print(f'{result}')
