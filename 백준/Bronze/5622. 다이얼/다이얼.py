word = input()
# 다이얼 전화기와 같이 짝지어진 str을 리스트로 만들고
check_lst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
answer = 0
for _ in word:
    # 반복문을 돌면서 입력값의 각 알파벳들이 어디에 있는지 체크
    for check in check_lst:
        if _ in check:
            # 인덱스 값을 반환해서 걸리는 시간에 맞게 값을 더해줌
            answer += check_lst.index(check) + 3
# 총 걸리는 시간 출력
print(answer)