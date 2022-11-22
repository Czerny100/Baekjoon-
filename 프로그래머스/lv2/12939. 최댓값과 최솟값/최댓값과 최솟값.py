def solution(s):
    # split 함수로 리스트 생성
    lst = s.split(' ') 
    # 근데 요소값이 str 형태니까 map 함수로 정수가 담긴 리스트로 변환
    new_lst = list(map(int,lst))
    
    # 변수 생성해서 max랑 min함수로 원하는 값 저장
    _max = max(new_lst)
    _min = min(new_lst)

    # 형태에 맞게 answer 만들어줌
    answer = str(_min)+' '+str(_max)
    return answer