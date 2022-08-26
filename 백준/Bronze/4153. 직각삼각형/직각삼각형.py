while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if a>=c and a>=b:
        a,c = c,a
    elif b>=c and b>=a:
        b,c = c,b
    if (c*c == a*a + b*b):
        print('right')
    else:
        print('wrong')

