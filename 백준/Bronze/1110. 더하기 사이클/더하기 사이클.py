import sys
# 입력받은 값을 정수로 저장하고 새로운 변수에도 저장, cnt는 사이클 길이
N = int(sys.stdin.readline())
new_N = N
cnt = 0

while True:
    # 주어진 규칙에 따라 new_N%10*10는 십의 자리, (new_N//10+new_N%10)%10는 일의 자리
    # 사이클 길이를 1씩 늘리면서 while문 반복, 첫 값과 같아질 때 종료
    new_N = new_N%10*10 + (new_N//10+new_N%10)%10
    cnt += 1
    if new_N == N:
        print(cnt)
        break