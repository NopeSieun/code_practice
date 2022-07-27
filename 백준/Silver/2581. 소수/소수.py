a = int(input())
b = int(input())

c = []

def test(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for j in range(2,x):
            if x%j==0:
                return False
        return True

for i in range(a,b+1):
    if test(i) == True:
        c.append(i)
        
if len(c)==0:
    pass
else:
    print(sum(c))

print(-1) if len(c) == 0 else print(min(c))