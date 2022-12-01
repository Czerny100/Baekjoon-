word = input()
# 특수형태 크로아티안 알파벳은 몇개 안되니까 문자열 리스트로 작성
check_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# 반복문을 돌면서 크로아티안 알파벳이 있으면 전부 'a'로 바꿔버림. 위 목록에 없는 알파벳은 한 글자씩 센다니까 상관없음!
for alpha in check_list:
    word = word.replace(alpha,'a')
# 바뀐 문자열의 길이를 구하면 크로아티안 알파벳이 몇 개인지 알 수 있음
print(len(word))