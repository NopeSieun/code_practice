s = int(input())

for i in range(s):
    a,b = list(input().split())
    a = int(a)
    b = str(b)
    for j in b:
        print(a*j,end='')
    print()