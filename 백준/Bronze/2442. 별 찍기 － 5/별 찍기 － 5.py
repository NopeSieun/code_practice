N = int(input())

for i in range(1, N+1):
    star = '*'
    print(" "*(N-i)+star*((2*i)-1))