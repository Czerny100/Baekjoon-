# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
N = int(input())
# 둘째 줄에는 정수가 공백으로 구분되어져있다. 입력받은 값을 공백으로 구분해 lst에 저장.
lst = list(map(int, input().split()))
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
v = int(input())
cnt = 0
# list를 돌면서 해당 요소가 v값과 같으면 cnt +1
for i in lst:
    if i == v:
        cnt += 1
print(cnt)