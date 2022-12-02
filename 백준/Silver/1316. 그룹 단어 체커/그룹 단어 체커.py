# str 내에서 문자가 연속하여 나타나는 부분을 제거하는 함수
def shorten_str(str):
    new_str = str[0]
    for i in range(1,len(str)):
        if str[i] == str[i-1]:
            continue
        new_str += str[i]
    return new_str
# 연속된 부분이 제거 된 상태에서 중복이 나타나는 경우는 groupword가 아니므로 0을 반환하고, 아닌 경우 1을 반환하는 함수
def isgroupword(str):
    for _ in str:
        if str.count(_) > 1:
            return(0)
        else:
            continue
    return(1)
# N만큼 입력을 받고 입력받은 문자열이 groupword인 경우에만 cnt값을 1씩 늘려줌
N = int(input())
cnt = 0
for i in range(N):
    input_str = input()
    cnt += isgroupword(shorten_str(input_str))
print(cnt)