n = int(input())
b = list(map(int,input().split()))
c = 0
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

for i in b:
    if test(i) == True:
        c+=1
        
print(c)