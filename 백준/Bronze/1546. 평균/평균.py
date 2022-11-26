import statistics
# 과목 수 N을 입력받고
N = int(input())
# N개 만큼 특정값을 입력받고
lst = list(map(int, input().split()))
M = max(lst)
# 각 점수 값을 점수/M*100로 바꿔치기 한 뒤에
new_lst = [lst[i]/M*100 for i in range(N)]
# 다시 구한 평균값을 출력
print(statistics.mean(new_lst))
