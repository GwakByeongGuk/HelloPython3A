# 단위 환산
def convertUnit(mm):
    conversion_rates = {
        'cm': 0.1,
        'm': 0.001,
        'inch': 0.03937,
        'ft': 0.00328084
    }
    conversions = {}
    for unit, rate in conversion_rates.items():
        conversions[unit] = mm * rate
    return conversions

def readUnit():
    mm = int(input("길이(mm)를 입력하세요"))
    return mm

def printUnit(mm, converesions):
    for unit, value in converesions.items():
        print(f'{mm} mm --> {value:.5f} {unit}')

mm = readUnit()
conversions = convertUnit(mm)
printUnit(mm, conversions)



# 할인된 상품 출력
def discountPrices(discount, prices):
    discount_prices = []
    for price in prices:
        discounted_price = price - (price * discount / 100)
        discount_prices.append(discounted_price)
    return discount_prices

def readPrices():
    products = ['쌀', '상추', '고추', '마늘', '통닭', '햄', '치즈']
    prices = [9900, 1900, 2900, 8900, 5600, 6900, 3900]
    return products, prices

def printPrices():
    discount = int(input('오늘의 할인율을 입력하세요: '))
    products, prices = readPrices()
    discounted_prices = discountPrices(discount, prices)

    print(f'''
-------------------------------------------
-- 한빛마트 오늘의 할인 가격표 출력 시스템 --
-------------------------------------------
오늘의 할인율을 입력하세요. {discount}%
''', end='')
    for i in range(len(products)):
        print(f'{products[i]:<6} {prices[i]:>10,} 원 {discount:>7}%DC -> {discounted_prices[i]:>10,.0f} 원')

    print('-' * 46)

printPrices()



def checkJumin(jumin_numbers):
    # 앞 12자리에 곱할 숫자들
    mul = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    # 각 자리 숫자와 곱할 숫자를 곱한 값을 모두 더합니다.
    total = sum(num * multipl for num, multipl in zip(jumin_numbers[:12], mul))

    # 결과값을 11로 나눈 나머지를 11에서 뺍니다.
    remainder = total % 11
    check_digit = (11 - remainder) % 10

    # 계산된 검증 숫자와 실제 주민등록번호의 마지막 자리를 비교합니다.
    return check_digit == jumin_numbers[12]

def readJumin():
    jumin = input("주민등록번호를 입력하세요 (*************): ")
    jumin_numbers = [int(num) for num in jumin if num.isdigit()]
    return jumin_numbers

def printJumin():
    jumin_numbers = readJumin()

    # 입력받은 주민등록번호의 길이가 13인지 확인
    if len(jumin_numbers) != 13:
        print("유효하지 않은 주민등록번호입니다.")
    else:
        # 주민등록번호 유효성 검사
        valid = checkJumin(jumin_numbers)
        # 결과 출력
        if valid:
            print("유효한 주민등록번호입니다.")
        else:
            print("유효하지 않은 주민등록번호입니다.")

printJumin()


