# 테스트 케이스 갯수 C을 입력받자
C = int(input())
# 점수가 들어갈 리스트 생성
score = []
# 테스트 케이스 갯수만큼 반복문을 진행하면서 score에 학생수 N과 점수를 입력
for i in range(C):
    score = list(map(int,input().split()))
    # 맨 첫번째 값은 학생 수 N
    N = score[0]
    score_avg = (sum(score) - N)/N
    cnt = 0
    for j in range(1,N+1):
        if score[j] > score_avg:
            cnt += 1
    answer = (cnt/N)*100
    # round로 하면 소수점 없이 딱 맞아 떨어질 때 뒤에 .00이 출력이 안됨
    print(format(answer,'.3f')+'%')