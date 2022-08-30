k,q,r,b,kn,p = map(int,input().split())
#1,1,2,2,2,8 개가 기본 구성 

if k!=1:
    print(1-k,end=' ')
else:
    print(0,end=' ')

if q!=1:
    print(1-q,end=' ')
else:
    print(0,end=' ')

if r!=2:
    print(2-r,end=' ')
else:
    print(0,end=' ')

if b!=2:
    print(2-b,end=' ')
else:
    print(0,end=' ')

if kn!=2:
    print(2-kn,end=' ')
else:
    print(0,end=' ')

if p!=8:
    print(8-p)
else:
    print(0)