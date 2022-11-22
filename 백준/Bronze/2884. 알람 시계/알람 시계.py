H, M = map(int, input().split())
print((24+H-(M<45))%24,(M-45)%60)