N = int(input())

su = 0
while N>=0:
    if N%5==0:
        su+=(N//5)
        print(su)
        break
    N-=3
    su+=1
else:
    print(-1)#while문 거짓일 경우 -1