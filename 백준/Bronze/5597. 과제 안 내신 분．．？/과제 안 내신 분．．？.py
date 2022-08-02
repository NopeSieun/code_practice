cnt = []

for _ in range(28):
    num = int(input())
    cnt.append(num)
cnt.sort()
    
for i in range(1,31):
    if i in cnt:
        pass
    else:
        print(int(i))