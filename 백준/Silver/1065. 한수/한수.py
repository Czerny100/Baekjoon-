# 양의 정수 X의 각 자리가 등차수열을 이루는 수 => 한수
# 자연수 N이 주어졌을 때 1보다 크거나 같고 N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오

N = int(input())
cnt = 0

# [1] 1<= N <= 99 인 경우 모두 한수이므로 그대로 N을 출력
if 0 < N < 100:
    print(N)
# [2] 100 <= N 인 경우 100부터 N까지의 수를 돌면서 각 자리 수를 분리해 리스트에 저장
else :
    for i in range(100, N+1):
        N_list = [int(a) for a in str(i)]
        # N의 범위가 문제에서는 제한되어 있으므로 이미 한수가 아닌 1000은 제외, 세자리수 수라고 생각하고 인덱스 기준으로 차가 같으면 cnt를 1씩 증가시킴
        if N_list[1]-N_list[0] == N_list[2]-N_list[1]:
            cnt += 1
    # 100보다 작은 한수의 값을 더해서 출력
    print(cnt+99)