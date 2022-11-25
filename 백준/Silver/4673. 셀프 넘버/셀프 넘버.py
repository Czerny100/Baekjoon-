# d(n) => n과 n의 각 자리수를 더하는 함수
# d(75) = 75(n) + 7(n//10) + 5(n%10) = 87
# n을 d(n)의 생성자라고 할 때, 생성자가 없는 숫자를 셀프 넘버라고 한다.
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 생성자의 정의에 맞는 함수 만들기
def dn(n):
    sum = n
    for _ in str(n):
        sum += int(_)
    return(sum)

# 딕셔너리 하나 생성, 이때 dic의 value값은 키값 i의 생성자인 경우 1이 됨
# 한번도 생성자가 아닌 셀프 넘버(value값이 0인 key)들만 출력
check_dic = {}

for i in range(1,10001):
    check_dic[i] = 0
for i in range(1,10001):
    check_dic[dn(i)] = 1
for i in range(1,10001):
    if check_dic[i] == 0:
        print(i)