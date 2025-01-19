score_list = []  # 과목들의 정보를 저장할 리스트

# 20개의 과목 정보 입력받기
for i in range(20):
    score_input = list(map(str, input().split()))  # 입력값을 공백으로 나누고 리스트로 변환
    score_list.append(score_input)  # 입력받은 과목 정보(score_input)를 score_list에 추가

# 학점에 대응하는 점수 테이블 (딕셔너리 형태)
score_table = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0
}

# 총 점수와 총 이수 학점 초기화
total_score = 0  # 누적 점수
total_credits = 0  # 누적 이수 학점

# 각 과목에 대해 점수 계산
for row in score_list:
    grade = row[2]  # 학점(row[2])
    credits = float(row[1])  # 이수 학점(row[1])
    
    # 학점에 맞는 점수 찾기
    if grade in score_table:
        total_score += score_table[grade] * credits  # 학점에 해당하는 점수 * 이수 학점
        total_credits += credits  # 이수 학점 누적

# 평균 평점 계산

average_score = total_score / total_credits  # 총 점수 / 총 이수 학점
print(f"{average_score:.6f}")  # 소수점 6자리까지 출력