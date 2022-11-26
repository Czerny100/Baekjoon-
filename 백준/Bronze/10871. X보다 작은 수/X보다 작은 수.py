import sys

# 문제 조건에 따라 입력 받기
N, X = map(int, sys.stdin.readline().split())
lst = map(int, sys.stdin.readline().split())
# 조건에 맞는 값(X보다 작은 값)이 들어갈 빈 리스트 생성
new_lst = []
# 반복문을 돌면서 lst의 요소가 X보다 작을 때 빈 리스트에 추가시켜줌
for i in lst:
    if i < X:
        new_lst.append(i)
# 조건에 맞는 형태로 출력
print(' '.join(str(j) for j in new_lst))
