n = int(input())
num = list(map(int,input().split()))
find = int(input())
c = 0 

for i in num:
    if i == find:
        c += 1
print(c)