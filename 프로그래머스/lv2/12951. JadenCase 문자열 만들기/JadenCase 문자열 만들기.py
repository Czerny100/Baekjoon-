def solution(s):
    answer = ''
    # split으로 나누어 리스트에 문자열 형태로 담음
    lst = s.split(' ')
    # 바뀐 문자열을 담을 빈 리스트 생성
    new_lst = []
    # 반복문 돌리면서 조건에 맞게 문자열 변환
    for word in lst:
        word = word.capitalize()
        # 빈 리스트에 변환된 문자열 추가
        new_lst.append(word)
    # join으로 조건에 맞는 리턴값 만들기
    answer = ' '.join(new_lst)
    return answer