num1 = set(range(1,10000))
num2 = set()

for num in num1:
    for n in str(num): #ex) 39 = 3 + 9 
        num += int(n)
    num2.add(num)

selfnum = num1 - num2
for selfn in sorted(selfnum):
    print(selfn)
