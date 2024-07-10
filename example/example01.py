# 실전예제 1
email = 'gildong@abc123.co.kr'
name = '홍길동'
userid = 'gildong'
passwd = '1234'

# print(f'To. {email}')
# print(f'▶ 아이디 및 비밀번호 확인')
# print(f'  {name} 고객님 안녕하세요')
# print(f'  {name} 고객님의 아이디와 비밀번호는 아래와 같습니다')
# print(f'  아이디 : {userid}')
# print(f'  비밀번호 : {passwd}')

print(f'''To. {email}
▶ 아이디 및 비밀번호 확인
  {name} 고객님 안녕하세요
  {name} 고객님의 아이디와 비밀번호는 아래와 같습니다
  아이디 : {userid}
  비밀번호 : {passwd}''')


# 실전예제 2
day = input('요일은? ')
date = input('날짜(월일)는? ')
minTemp = input('최저 기온은? ')
maxTemp = input('최고 기온은? ')
rainy = input('비올확률은? ')
dusty = input('미세먼지는? ')
riseSun = input('일출시간은? ')
downSun = input('일몰시간은? ')
southWave = input('남해 물결높이는? ')
eastWave = input('동해 물결높이는? ')
westWave = input('서해 물결높이는? ')

print(f'''내일 날씨 예보입니다.
{day}요일인 {date}의 아침 최저 기온은 {minTemp}도, 낮 최고 기온은 {maxTemp}도로 예보됐습니다.
비올 확률은 {rainy}%이고, 미세먼지는 {dusty} 수준일 것으로 예상됩니다.
일출 시간은 {riseSun}이고, 일몰 시간은 {downSun}입니다.
바다의 물결은 남해 앞바다 {southWave}m, 동해 앞바다 {eastWave}m, 서해 앞바다 {westWave}m 높이로 일겠습니다.
지금까지 {date} {day}요일 날씨 예보였습니다.''')


# 영수증 예제
date = '2014. 07. 07 14:35:24'
soju = 2
chiken = 1

total = (soju * 3000) + (chiken * 12000)
vat = total * (10/110) #부가세 = 합계금액 * 0.1
supply = total - (100/110) # 공급가액 = 합계급액 - 부가세

paid = 50000
charge = paid - total

print(f'''
[음식나라]
-----------------
소주\t\t{soju}\t\t{soju * 3000}
너나치킨\t{chiken}\t\t{chiken * 12000}
-----------------
과세합계\t\t\t{int(supply)}
부가세\t\t\t{int(vat)}
-----------------
총합계\t\t\t{total}
받은금액\t\t\t{paid}
잔돈\t\t\t{charge}
-----------------
{date}
''')

# 3 - 사용가능 변수 알아보기
rate1 = 123
# 1stPlayer = 456
# myprogram.java = 789
long = 987
# except = 654
TimeLimit = 321
numberOfWindows = 1000


# 11 - 이름, 몸무게, 나이를 변수로 선언하고 초기화
name = '일지매'
weight = 45.5
age = 35

print(name, weight, age)


# 12 - 생년월일 계산
# 연나이 계산 : 현재년도 - 태어난년도 (병역법,교육법,민방위)
# 만나이 : 현재년도 - 태어난년도, 생일안지남 (-1) (민법상, 2023-06부터)
# 한국식 나이 : 현재년도 - 태어난년도 + 1
currentYear = int(input('현재년도는? '))
birthYear = int(input('생일의 년도는? '))
myAge = currentYear - birthYear

print(f'''현재년도가 {currentYear}이고, 
생일의 년도가 {birthYear}일 때, 
나이는 {myAge} 입니다.''')

# 13 - 구구단 7단 출력

# print('7 x 1 = 7')
# print('7 x 2 = 14')
# print('7 x 3 = 21')
# print('7 x 4 = 28')
# print('7 x 5 = 35')
# print('7 x 6 = 42')
# print('7 x 7 = 49')
# print('7 x 8 = 56')
# print('7 x 9 = 63')

# dan = 7
# print(f'{dan} x 1 = {dan * 1}')
# print(f'{dan} x 2 = {dan * 2}')
# print(f'{dan} x 3 = {dan * 3}')
# print(f'{dan} x 4 = {dan * 4}')
# print(f'{dan} x 5 = {dan * 5}')
# print(f'{dan} x 6 = {dan * 6}')
# print(f'{dan} x 7 = {dan * 7}')
# print(f'{dan} x 8 = {dan * 8}')
# print(f'{dan} x 9 = {dan * 9}')

dan = 7
print(f'''
{dan} x 1 = {dan * 1}
{dan} x 2 = {dan * 2}
{dan} x 3 = {dan * 3}
{dan} x 4 = {dan * 4}
{dan} x 5 = {dan * 5}
{dan} x 6 = {dan * 6}
{dan} x 7 = {dan * 7}
{dan} x 8 = {dan * 8}
{dan} x 9 = {dan * 9}''')







