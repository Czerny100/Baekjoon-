X = int(input())
Y = int(input())
sum = 0
for i in range(Y):
    price, qty = map(int, input().split())
    sum += price * qty
print('Yes' if X == sum else 'No')