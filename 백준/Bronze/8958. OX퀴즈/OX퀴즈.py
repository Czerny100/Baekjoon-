# 테스트 케이스 갯수 N을 입력받자
N = int(input())
# O랑 X로 이루어진 str을 매개변수로 하는 함수 만들어줌
def solution(str):
    # X를 기준으로 문자열을 자르면 요소가 O으로만 이루어진 문자열 혹은 공백문자열인 리스트가 만들어짐
    lst = str.split('X')
    # 일단 리턴할 sum값 초기화
    sum = 0
    # 생성된 lst를 돌면서 O이 연속될 때마다 점수가 1씩 늘어나고, 그 점수값을 sum에 더해줌 O가 아닌 경우 반복문을 탈출해 score 초기화
    for i in lst:
        score = 0
        for j in range(len(i)):
            if i[j] == 'O':
                score += 1
                sum += score
            else:
                break
    # 반복문 끝나면 sum값 return
    return sum
# N만큼 반복한 함수값을 출력
for i in range(N):
    print(solution(input()))


