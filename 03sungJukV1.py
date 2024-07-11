 # 성적 처리 프로그램 v1
 # 이름, 국어, 영어, 수학을 입력 받으면
 # 총점, 평균, 학점을 계산하고 출력함
 # 학점 : 수우미양가

 # 이름 : 홍길동, 국어 : 99, 영어 : 98, 수학: 99
 # 총점 : 296, 평균: 98.6, 학점 : 수

 # 성적 데이터 입력받음
Name = input('이름을 입력하세요: ')
Kor = int(input('국어: '))
Eng = int(input('영어: '))
Math = int(input('수학: '))

Sum = int(Kor+Eng+Math); Avg = round(float((Sum)/3),2)
def grade_suumiyangga(Avg):
    if Avg >= 90:
        return "수"
    elif Avg >= 80:
        return "우"
    elif Avg >= 70:
        return "미"
    elif Avg >= 60:
        return "양"
    else:
        return "가"

print(f'''
이름 : {Name}
국어 성적 : {Kor}, 영어 성적 : {Eng}, 수학 성적 : {Math}
총점 : {Sum}, 평균 : {Avg} 학점 : {grade_suumiyangga(Avg)}
''')

# 성적 데이터 입력 받음
name = input('이름을 입력하세요: ')
kor = int(input('국어: '))
eng = int(input('영어: '))
mat = int(input('수학: '))
# 성적 처림
tot = kor + eng + mat
avg = tot/3
grd = '수' if (avg >= 90) else '우' if (avg >= 80) else \
      '미' if (avg >= 70) else '양' if (avg >= 60) else '가'
#결과출력
print(f'''
이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {mat}
총점 : {tot}, 평균 : {avg:.1f}, 학점 : {grd}
''')