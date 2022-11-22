import sys
lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, line.split())
    print(A+B)

# 다른 방법
import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except :
        break
