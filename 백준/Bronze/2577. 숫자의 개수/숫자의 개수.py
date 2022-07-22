num1 = int(input())
num2 = int(input())
num3 = int(input())

mult = list(str(num1*num2*num3))

for i in range(10):
    print(mult.count(str(i))) #count함수는 문자열에서만 사용 가능하다