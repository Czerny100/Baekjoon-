T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    if N%H == 0:
        room_num = str(N//H).zfill(2)
        print(f"{H}{room_num}")
    else:
        room_num = str((N//H+1)).zfill(2)
        print(f"{N%H}{room_num}")