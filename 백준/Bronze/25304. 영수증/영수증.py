s = int(input())
n = int(input())
price_ = []

for _ in range(n):
    price, m = map(int,input().split())
    price_.append(price*m)

if sum(price_) == s:
    print('Yes')
else:
    print('No')