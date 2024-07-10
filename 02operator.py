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