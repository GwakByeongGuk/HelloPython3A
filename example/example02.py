# 4 수학식을 파이썬 표현식으로 바꿔보아라
x = 1; y = 2; z = 3
s0 = 1; y0 = 2; g = 9.8; t = 3

a = 3 * x
b = 3 * x + y
c = (x+y) /7
d = (3*x+y)/(z+2)
e = s0 + y0 + 1/2*g*t**2
# 5~10

# 12 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라
# 만나이 : 현재년도 - 태어난년도, 생일안지남(-1)
currentYear = int(input('현재년도는? '))
birthYear = int(input('생일의 년도는? '))
isPass = bool(input('생일 지남 여부는? (True/False)'))

myAge = currentYear - birthYear
# maAge = myAge if (isPass == True) else (myAge - 1)
maAge = myAge if isPass else (myAge - 1)

print(f'''현재년도가 {currentYear}이고,
생일의 년도가 {birthYear}일 때,
나이는 {myAge}입니다.''')

# 한국식 나이 : 현재년도 - 태어난년도 + 1
currentYear = int(input('현재년도는? '))
birthYear = int(input('생일의 년도는? '))
myAge = currentYear - birthYear

print(f'''현재년도가 {currentYear}이고,
생일의 년도가 {birthYear}일 때,
나이는 {myAge}입니다.''')

# 14
day = 86400   # 하루 - 초
hour = 3600   # 시간 - 초
minute = 60   # 분 - 초

days = 1234567890 / day
hours = 98765 / hour
minutes = 12345 / minute
print (f'''{int(days):,}일,
{int(hours):,}시간,
{int(minutes):,}분
''')
# 16 (!!)
price = 34_560
paid = 50_000
charge = paid - price

w50000 = 0; w10000 = 0; w5000 = 0
w1000 = 0; w500 = 0; w100 = 0; w50 = 0; w10 = 0

# w50000 = charge / 50000      # 결과는 float
# w50000 = int(charge / 50000) # 결과를 정수형으로 반환
w50000 = charge // 50000       # 파이썬의 몫 연산자
#charge = charge - (50000 * w50000)
charge %= 50000
w10000 = charge // 10000
charge = charge - (10000 * w10000)
w5000 = charge // 5000
charge = charge - (5000 * w5000)
w1000 = charge // 1000
charge = charge - (1000 * w1000)
w500 = charge // 500
charge = charge - (500 * w500)
w100 = charge // 100
charge = charge - (100 * w100)
w50 = charge // 50
charge = charge - (50 * w50)
w10 = charge // 10
charge = charge - (10 * w10)

print(f'''
금액 : {price:,} 원
지불금액 : {paid:,} 원
잔돈 : {(paid-price):,} 원
-----------
50000원 : {w50000} 장
10000원 : {w10000} 장
5000원 : {w5000} 장
1000원 : {w1000} 장
500원 : {w500} 개
100원 : {w100} 개
50원 : {w50} 개
10원 : {w10} 개
''')

# GPT
def calculate_change(change):
    denominations = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = {}

    for denomination in denominations:
        count = change // denomination
        change %= denomination
        result[denomination] = count

    return result

def print_change(change):
    result = calculate_change(change)
    for denomination in sorted(result.keys(), reverse=True):
        print(f"{denomination}원: {result[denomination]}개")

if __name__ == "__main__":
    change = int(input("잔돈을 입력하세요: "))
    print_change(change)