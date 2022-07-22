n = int(input())
num = n
count = 0

while True:
    count+=1
    sum = n//10 + n%10 #10의자리수:몫, 1의자리수:나머지
    n = n%10*10 + sum%10
    if (n == num):
        break
print(count)