# 값을 받아 리스트로 만들고
# 각 값을 42로 나눈 나머지로 바꾸고
lst = []
for i in range(1,11):
    lst.append(int(input())%42)
# set 함수 사용해서 중복 제거해버리고
# 요소의 개수를 출력하면 되지않을까?
print(len(set(lst)))
