# 첫줄에 입력 받을 숫자 N이 주어짐
# 둘째줄에 숫자 N개가 공백 없이 주어짐
# N만큼 반복하면서 인덱스 기준으로 더해주면 될듯?

N = int(input())
num = input()
print(sum((int(i) for i in num)))