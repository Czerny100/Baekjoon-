def find_slope(lst1,lst2):
    slope = (lst1[1]-lst2[1])/(lst1[0]-lst2[0])
    return slope

def solution(dots):
    answer = 0
    if find_slope(dots[0],dots[1]) == find_slope(dots[2],dots[3]):
        answer = 1
    elif find_slope(dots[0],dots[2]) == find_slope(dots[1],dots[3]):
        answer = 1
    elif find_slope(dots[0],dots[3]) == find_slope(dots[1],dots[2]):
        answer = 1
    return answer