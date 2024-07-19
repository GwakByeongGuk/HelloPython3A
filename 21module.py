# 모듈
# 매우 복잡하고 긴 코드를 하나의 파일에
# 모두 작성하는 것은 비효율적임 - 유지보수 힘듦
# 또한, 여러 사람들과 함꼐 개발하는 경우
# 작업분담, 작업결과물 통합 역시 어려움

# 모듈방식의 개발을 이용하면
# 사용용도에 따라 파일별로 나눠 작성 가능
# 타인이 만들어 둔 코드를 자신의 프로그램에서 활용 가능
# 따라서, 모듈은 변수/함수/클래스들을 모아둔 파일

# 모듈은 현재 디렉토리에 있는 파일이나
# 파이썬 라이브러리 디렉토리에 있는 파일을 불러올 수 있음
# 사용자/venv/py310/Lib/site-package

# 모듈 불러오기
# import 명령을 이용해서 불러올 수 있음
# 모듈내 정의된 함수/클래스를 사용하려면
# 모듈명.함수명, 모듈명.클래스 형식으로 코드 작성
# import ashwoo.hello
#
# ashwoo.hello.sayHello()
#
# # ---
#
# from ashwoo2 import hello2
#
# hello2.sayHello2()


# 모듈사용하기 1 - 모듈명.함수명
import ashwoo.calc

val = ashwoo.calc.add(10, 5)
print(val)

# 모듈사용하기 2 - 함수명
from ashwoo.calc import add
from ashwoo.calc import div

val = add(10, 5)
print(val)
val = div(10, 5)
print(val)

# 모듈사용하기 3 - 함수명
from ashwoo.calc import *

val = mul(10, 5)
print(val)
val = minus(10, 5)
print(val)

# 모듈사용하기 3 - 별칭
import ashwoo.calc as zc

val = zc.add(10, 20)
print(val)

# 외부 모듈 사용하기
# 내장모듈이나 사용자 정의 모듈 이외의
# 다른조직/기관이나 개인이 만든 모듈을 사용하려면
# 'pip install 모듈명'으로 설치할 수 있음
# pip install scikit-learn
# pip install pymysql
# pip install fastapi

# ashwoo.example 에 각 문제에대한 모듈 작성

# 단위 환산
# (convertUnit/readUnit/printUnits)
import ashwoo.example as aex
mm = aex.readUnit()
conversions = aex.convertUnit(mm)
aex.printUnit(mm, conversions)


# 할인된 상품 가격표 출력
# (discountPrices/readPrices/printPrices)
import ashwoo.example as aex
aex.printPrices()



# 주민번호 유효성 체크
# (checkJumin/readJumin/printJumin)
# 주민등록번호는 13자리로 이루어져 있으며, 앞 6자리는 생년월일, 뒤 7자리 중 첫 번째 숫자는 성별 코드, 나머지 6자리는 지역 및 순서 코드를 의미합니다. 유효한 주민등록번호인지 확인하기 위해서는 다음과 같은 규칙을 따릅니다.
#
# 주민등록번호 길이가 13자리인지 확인합니다.
# 뒤 7자리 중 첫 번째 숫자가 1, 2, 3, 4 중 하나인지 확인합니다. (1, 3은 남자, 2, 4는 여자를 의미)
# 뒤 7자리 중 첫 번째 숫자를 제외한 나머지 6자리가 유효한 값인지 확인합니다. (000001 ~ 899999 사이의 값)
# 주민등록번호 유효성 검사 공식에 따라 계산한 결과가 맞는지 확인합니다.
# 이 때 주민등록번호 유효성 검사 공식은 다음과 같습니다.
#
# 주민등록번호 앞 12자리에
# 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 곱한 값을
# 모두 더합니다.
# 그 결과값을 11로 나눈 나머지를 11에서 뺍니다.
# 계산 결과값이 주민등록번호 마지막 자리 숫자와 일치하면 유효한 주민등록번호입니다.
# 위 규칙에 따라 주민등록번호 유효성을 검사하는 프로그램을 작성해 보세요.

# 1 2 3 4 5 6 - 1 2 3 4 5 6 7
# * * * * * *   * * * * * *
# 2 3 4 5 6 7   8 9 2 3 4 5
# 2+6+12+20+30+42 +8+18+6+12+20+30
# 11 - (206 % 11) = 3
import ashwoo.example as aex
aex.printJumin()

# aex.printJumin2('123456-1234567')


