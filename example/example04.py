# 51 구구단

Multiplication_Table = f'''
      1   2   3   4   5   6   7   8   9
========================================
1 | {{1_1:3d}} {{1_2:3d}} {{1_3:3d}} {{1_4:3d}} {{1_5:3d}} {{1_6:3d}} {{1_7:3d}} {{1_8:3d}} {{1_9:3d}}
2 | {{2_1:3d}} {{2_2:3d}} {{2_3:3d}} {{2_4:3d}} {{2_5:3d}} {{2_6:3d}} {{2_7:3d}} {{2_8:3d}} {{2_9:3d}}
3 | {{3_1:3d}} {{3_2:3d}} {{3_3:3d}} {{3_4:3d}} {{3_5:3d}} {{3_6:3d}} {{3_7:3d}} {{3_8:3d}} {{3_9:3d}}
4 | {{4_1:3d}} {{4_2:3d}} {{4_3:3d}} {{4_4:3d}} {{4_5:3d}} {{4_6:3d}} {{4_7:3d}} {{4_8:3d}} {{4_9:3d}}
5 | {{5_1:3d}} {{5_2:3d}} {{5_3:3d}} {{5_4:3d}} {{5_5:3d}} {{5_6:3d}} {{5_7:3d}} {{5_8:3d}} {{5_9:3d}}
6 | {{6_1:3d}} {{6_2:3d}} {{6_3:3d}} {{6_4:3d}} {{6_5:3d}} {{6_6:3d}} {{6_7:3d}} {{6_8:3d}} {{6_9:3d}}
7 | {{7_1:3d}} {{7_2:3d}} {{7_3:3d}} {{7_4:3d}} {{7_5:3d}} {{7_6:3d}} {{7_7:3d}} {{7_8:3d}} {{7_9:3d}}
8 | {{8_1:3d}} {{8_2:3d}} {{8_3:3d}} {{8_4:3d}} {{8_5:3d}} {{8_6:3d}} {{8_7:3d}} {{8_8:3d}} {{8_9:3d}}
9 | {{9_1:3d}} {{9_2:3d}} {{9_3:3d}} {{9_4:3d}} {{9_5:3d}} {{9_6:3d}} {{9_7:3d}} {{9_8:3d}} {{9_9:3d}}
========================================
'''

for i in range(1, 10):
    for j in range(1, 10):
        replace = f'{i}_{j}'
        Multiplication_Table = Multiplication_Table.replace(f'{{{replace}:3d}}', f'{i*j:3d}')

print(Multiplication_Table)

def multiplication():
    result = ''
    for i in range(1, 10):
        row = ''
        for j in range(1, 10):
            row += f'{j * i:2d} '
        result += f'{i} | {row}\n'
    return result

Multiplication_Table2 = f'''
       Mutilplication Table
     1  2  3  4  5  6  7  8  9
===============================
{multiplication().strip()}
===============================
'''

print(Multiplication_Table2)

print('''
            Multiplication Table
      1   2   3   4   5   6   7   8   9
------------------------------------------
1 | 
2 | 
3 | 
4 | 
5 | 
6 | 
7 | 
8 | 
9 |
''')
print('''
            Multiplication Table
      1   2   3   4   5   6   7   8   9
------------------------------------------
''', end='')
for i in range(1, 10):
    print(f'{i} |   1   2   3   4   5   6   7   8   9')

print('''
            Multiplication Table
      1   2   3   4   5   6   7   8   9
------------------------------------------
''', end='')
for i in range(1, 10):
    print(f'{i} |',end='')
    for j in range(1, 10):
        print(f'{i*j:4d}', end='')
    print()


# 33
cardno = input('카드 번호는? ')

result = '잘못된 카드 번호입니다'
if cardno[0] == '3':
    if cardno == '356317':
        result = 'JCB카드 NH농협카드'
    elif cardno == '356912':
        result = 'JCB카드 KB국민카드'
if cardno[0] == '4':
    if cardno == '404825':
        result = '비자카드 비씨카드'
    elif cardno == '438676':
        result = '비자카드 신한카드'
    elif cardno == '457973':
        result = '비자카드 KB국민카드'
if cardno[0] == '5':
    if cardno == '515594':
        result = '마스터카드 신한카드'
    elif cardno == '524353':
        result = '마스터카드 외한카드'
    elif cardno == '540926':
        result = '마스터카드 KB국민카드'

print(f'{cardno} / {result}')

# 16 개선하기 - 리스트/반복문/함수

price = 34_560
paid = 50_000

def compute_charge(price, paid):
    changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = {}
    charge = paid - price
    for change in changes:
        count = charge // change
        charge %= change
        result[change] = count
    return result

def print_change(price, paid, change_count):
    print(f'''
금액 : {price:,} 원
지불금액 : {paid:,} 원
잔돈 : {(paid-price):,} 원
-----------
''')

    for result, count in change_count.items():
        if result >= 1000:
            print(f'{result:,}원 : {count} 장')
        else:
            print(f'{result}원 : {count} 개')

change_count = compute_charge(price, paid)
print_change(price, paid, change_count)

def compute_charge(price, paid):
    charges = []
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    charge = paid - price

    for money in moneys:
        charges.append(charge // money)
        charge %= money

    result = f'''
    금액 : {price:,} 원
    지불금액 : {paid:,} 원
    잔돈 : {paid-price:,} 원
    ------------
    '''
    for idx, m in enumerate(moneys):
        result += f'{m}원, {charges[idx]} 장/개\n'

    print(result)

# 잔돈 구하는 함수 호출 및 테스트
price = int(input('지불해야 할 금액은? '))
paid = int(input('받은 금액은? '))
compute_charge(price,paid)

