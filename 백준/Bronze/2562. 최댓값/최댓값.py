lst = []
for i in range(9):
    lst.append(int(input()))
max_num = sorted(lst)[-1]
print(max_num)
print(int(lst.index(max_num))+1)