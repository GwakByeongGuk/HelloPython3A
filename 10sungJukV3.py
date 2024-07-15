# 성적 처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함
# 학점 : 수우미양가

# 이름 : 민지, 국어 : 99, 영어 : 98, 수학: 99
# 이름 : 혜린, 국어 : 88, 영어 : 77, 수학: 66
# 이름 : 다니엘, 국어 : 55, 영어 : 77, 수학: 99

students = []

for i in range(1,3+1):
    name = input(f"학생 {i} 이름: ")
    kor = int(input(f"{name}의 국어 점수: "))
    eng = int(input(f"{name}의 영어 점수: "))
    math = int(input(f"{name}의 수학 점수: "))
    students.append({"이름": name, "국어": kor, "영어": eng, "수학": math})

print(students)

for j in students:
    tot = j["국어"] + j["영어"] + j["수학"]
    avg = tot / 3
    grd = '수' if avg >= 90 else '우' if avg >= 80 else \
        '미' if avg >= 70 else '양' if avg >= 60 else '가'

    print(f"\n이름: {j['이름']}")
    print(f"총점: {tot}")
    print(f"평균: {round(avg,1)}")
    print(f"학점: {grd}")
