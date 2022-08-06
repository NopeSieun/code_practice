num = list(map(int,input().split()))

def N(Num):
    new = []
    for i in Num:
        i *= i
        new.append(i)
    print(sum(new)%10)

N(num)