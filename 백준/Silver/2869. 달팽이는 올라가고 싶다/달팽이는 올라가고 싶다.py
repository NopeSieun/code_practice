a,b,v = map(int,input().split())
v -= b
if v%(a-b) == 0:
    print(v//(a-b))
else:
    print(v//(a-b)+1)