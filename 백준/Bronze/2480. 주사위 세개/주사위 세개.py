a, b, c = map(int,input().split())
if a==b==c:
    p = 10000+1000*a
elif a==b!=c or a==c!=b:
    p = 1000+100*a
elif b==c!=a:
    p = 1000+100*b
else:
    if a>b and a>c:
        p = 100*a
    elif b>a and b>c:
        p = 100*b
    else:
        p = 100*c
print(p)