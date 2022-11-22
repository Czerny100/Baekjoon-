def solution(A,B):
    answer = 0
    new_A = sorted(A)
    new_B = sorted(B, reverse=True)
    for i in range(len(A)):
        answer += int(new_A[i])*int(new_B[i])
    return answer