# 딕셔너리 한번 복습겸
check = {}
# 30명이니까 반복문 돌면서 value 값 초기화
for i in range(1,31):
    check[i] = 0
# 인풋값(key값)이 제출한 학생 번호이므로 해당 value값을 1로 바꿔줌
for j in range(1,29):
    check[int(input())] = 1
# value값이 0인 경우(제출하지 않은 학생)에만 오름차순 정렬하여 리스트에 저장
lst = sorted([k for k, v in check.items() if v == 0])
print(lst[0])
print(lst[1])