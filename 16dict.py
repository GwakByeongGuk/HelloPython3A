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
quizs = []
trueCount = 0
falseCount = 0
totalScore = 0

# 수학시험 프로그램

# 로또 당첨 게임