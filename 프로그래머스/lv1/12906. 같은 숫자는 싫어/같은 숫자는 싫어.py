def solution(arr):
    # 빈 리스트 생성
    new_arr = []
    # 맨 처음 값은 미리 추가해둠
    new_arr.append(arr[0])
    # 그 다음값부터 반복문 돌면서 이전값과 비교하여 중복이 아닌 값들만 새 리스트에 추가
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            new_arr.append(arr[i])
    return new_arr