T = int(input())
# 테스트 케이스로 똑같은 문자열이 주어질 때를 생각 못 했음
for i in range(T):
    new_word = ''
    N, S = input().split()
    for _ in S:
        new_word += _*int(N)
    print(new_word)