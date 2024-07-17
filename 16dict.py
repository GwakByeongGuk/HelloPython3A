# 딕셔너리
# 이름Key과 값Value으로 구성된 연관배열의 일종
# 자료구조를 만들 때는 {}를 사용하고
# 이름과 값은 : 으로 구분해서 정의함
# 다른 언어의 JSON과 유사한 구조
# 이름을 통해 자료를 찾는 해시테이블을 이용하므로 검색속도가 빠름

# 중간고사 성적을 dict로 선언
sj = {'C/C++':'A','Java':'B+','네트워크':'C',
      '보안':'A+','해킹':'F','클라우드':'C+'}
print(sj)

# 회원정보를 dict로 선언
# Key : 이름,아이디,비번,이메일,주소,취미

member = {'name': '홍길동', 'userid':'abc123',
          'passwd':'987xyz',
          'email':'abc123@987xyz.co.kr',
          'addr':'서울 관악구 봉천동',
          'hobby':['운동','게임','여행']}
print(member)

# 딕셔너리 다루기
# 조회 : 변수명[키], 변수명.get(키)
print(member['userid'],member['passwd'])
print(member.get('email'),member.get('addr'))

# 존재하지 않는 키 지정시
print(member['zipcode'])  #오류
print(member.get('dasd')) #None

# 새로운 항목 추가 : 변수명['새로운키'] = 값
member['zipcode'] = '12345'

# 기존 항목 수정 : 변수명['키'] = 수정할 값
member['zipcode'] = '98765'
member['addr'] = '서울 광진구 자양동'

# 기존 항목 삭제 : 변수명.pop(키)
member.pop('zipcode')
member.pop('addr')

# dict의 모든 키 조회 : 변수명.keys()
# dict의 모든 값 조회 : 변구명.values()
print(member.keys())
print(member.values())

# dict 전체항목 조회
for k in member.keys():
    print(f'{member[k]}', end=' ')

# 열거형enumerate으로 dict 조회 : 인덱스, 키
for idx, k in enumerate(member):
    print(idx, k)

# key와 value를 한번에 출력 : 변수명.items
for k, v in member.items():
    print(k, v)

# 중간고사 성적 관리
# 시나리오 #1
mids = {'C/C++':'A','Java':'B+','네트워크':'C',
      '보안':'A+','해킹':'F','시스템':'C+'}

# 시나리오 #2
print(f"Java : {mids['Java']}")
print(f"C/C++ : {mids['C/C++']}")

# 시나리오 #3
mids['파이썬'] = 'A'
mids['OS'] = 'A+'
print(mids)

# 시나리오 #4
mids['Java'] = 'F'
mids['시스템'] = 'A'
print(mids)

#시나리오 #5
for k in mids.keys():
    print(f'{k} : {mids[k]}')

for k, v in mids.items():
    print(f'{k} \t: {v}')

for k, v in mids.items():
    print(k, '\t: ',v)

# 수학시험 프로그램
quizs = ['3+2','5/2','10-2','10**2 * 2',
         '1-10%4','2**4','4/2']
score = [3,5,3,5,5,3,3]
#answer = [5,2.5,8,200,-1,16,2]
trueCount = 0
falseCount = 0
totalScore = 0
# enumerate : 반복 가능한 객체를 순회하면서,
# 각 요소의 위치값(인덱스)와 값을 함께 반환하는 함수
for i,quiz in enumerate(quizs):
    answer = eval(quiz)
    user_answer = float(input(f'{quiz} = '))
    if user_answer == answer:
        trueCount += 1
        totalScore += score[i]
        print('정답입니다')
    else:
        falseCount += 1
        print('오답입니다')
print(f'''
{'-'*20}
정답 개수 : {trueCount}
오답 개수 : {falseCount}
총 점수 : {totalScore}
{'-'*20}
''')
# 수학시험 프로그램 2
quizs = ((['3+2'],5,3),(['5/2'],2,5),(['10-2'],8,3),(['10**2 * 2'],200,5),
         (['1-10%4'],-1,5),(['2**4'],16,3),(['4/2'],2,3))
#answer = []
trueCount = 0
falseCount = 0
totalScore = 0
# enumerate : 반복 가능한 객체를 순회하면서,
# 각 요소의 위치값(인덱스)와 값을 함께 반환하는 함수
for i,quiz in enumerate(quizs):
    answer = eval(quiz)
    user_answer = float(input(f'{quiz} = '))
    if user_answer == answer:
        trueCount += 1
        totalScore += score[i]
        print('정답입니다')
    else:
        falseCount += 1
        print('오답입니다')
print(f'''
{'-'*20}
정답 개수 : {trueCount}
오답 개수 : {falseCount}
총 점수 : {totalScore}
{'-'*20}
''')

# 로또 당첨 게임
# 숫자 입력받기
# 로또 매직 넘버 생성
# 당첨 여부 확인
import random as rd
rd_num = rd.sample(range(1,46), 6)
rd_num.sort()
my_nums = []
while len(my_nums) < 6:
    my_num = int(input('1부터 45까지의 정수 6개를 입력하세요.'))
    if 1 <= my_num <= 45:
        if my_num != my_nums:
            my_nums.append(my_num)
        else:
            print('숫자가 중복되었습니다.')
    else:
        print('1부터 45를 입력하세요')

# for i in range(6):
#     my_num = int(input('1부터 45까지의 정수 6개를 입력하세요.'))
#     if 1 <= my_num <= 45:
#         if my_num != my_nums:
#             my_nums.append(my_num)
#             if len(my_nums) != 6:
#                 my_num = int(input('1부터 45까지의 정수 6개를 입력하세요.'))
#         else:
#             print('숫자가 중복되었습니다.')
#     else:
#         print('1부터 45를 입력하세요')
my_nums.sort()

matching_nums = set(rd_num) & set(my_nums)

matching_count = len(matching_nums)

if matching_count == 6:
    rank = "1등"
elif matching_count == 5:
    rank = "2등"
elif matching_count == 4:
    rank = "3등"
elif matching_count == 3:
    rank = "4등"
elif matching_count == 2:
    rank = "5등"
else:
    rank = "낙점"

print(f"이번주 로또 번호: {rd_num}")
print(f"내가 선택한 번호: {my_nums}")
print(f"일치하는 숫자: {sorted(matching_nums) if matching_nums else '없음'}")
print(f"등수: {rank}")