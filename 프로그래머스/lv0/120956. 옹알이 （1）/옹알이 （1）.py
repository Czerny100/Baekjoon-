def solution(babbling):
    babble_list = ['aya','ye','woo','ma']
    answer = 0
    for word in babbling:
        for i in babble_list:
            word = word.replace(i,'1',1)
        if word.isdigit():
            answer += 1
    return answer