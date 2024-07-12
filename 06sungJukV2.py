 # 성적 처리 프로그램 v2
 # 이름, 국어, 영어, 수학을 입력 받으면
 # 총점, 평균, 학점을 계산하고 출력함
 # 단, 학생 3명에 대해 성적처리를 진행함
 # 학점 : 수우미양가

 # 이름 : 민지, 국어 : 99, 영어 : 98, 수학: 99
 # 이름 : 혜린, 국어 : 88, 영어 : 77, 수학: 66
 # 이름 : 다니엘, 국어 : 55, 영어 : 77, 수학: 99


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
name1 = input('1번학생 이름: ')
kor1 = int(input('1번학생 국어: '))
eng1 = int(input('1번학생 영어: '))
mat1 = int(input('1번학생 수학: '))

name2 = input('2번학생 이름: ')
kor2 = int(input('2번학생 국어: '))
eng2 = int(input('2번학생 영어: '))
mat2 = int(input('2번학생 수학: '))

name3 = input('3번학생 이름: ')
kor3 = int(input('3번학생 국어: '))
eng3 = int(input('3번학생 영어: '))
mat3 = int(input('3번학생 수학: '))

# 성적 처림
tot1 = kor1 + eng1 + mat1
avg1 = tot1/3
grd1 = '수' if (avg1 >= 90) else '우' if (avg1 >= 80) else \
      '미' if (avg1 >= 70) else '양' if (avg1 >= 60) else '가'

tot2 = kor2 + eng2 + mat2
avg2 = tot2/3
grd2 = '수' if (avg2 >= 90) else '우' if (avg2 >= 80) else \
 '미' if (avg2 >= 70) else '양' if (avg2 >= 60) else '가'

tot3 = kor3 + eng3 + mat3
avg3 = tot3/3
grd3 = '수' if (avg3 >= 90) else '우' if (avg3 >= 80) else \
 '미' if (avg3 >= 70) else '양' if (avg3 >= 60) else '가'
#결과출력
print(f'''
이름 : {name1}, 국어 : {kor1}, 영어 : {eng1}, 수학 : {mat1}
총점 : {tot1}, 평균 : {avg1:.1f}, 학점 : {grd1}
이름 : {name2}, 국어 : {kor2}, 영어 : {eng2}, 수학 : {mat2}
총점 : {tot2}, 평균 : {avg2:.1f}, 학점 : {grd2}
이름 : {name3}, 국어 : {kor3}, 영어 : {eng3}, 수학 : {mat3}
총점 : {tot3}, 평균 : {avg3:.1f}, 학점 : {grd3}
''')