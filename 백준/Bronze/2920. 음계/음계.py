m = list(map(int, input().split()))
mi = 0
de = 0
asc = 0
for i in range(7):
    if m[i]+1 == m[i+1]:
        asc+=1
    elif m[i] == m[i+1] + 1:
        de+=1        
    else:
        mi+=1
        
if de==0 and mi==0:
    print('ascending')
elif asc==0 and mi==0:
    print('descending')
else:
    print('mixed')        