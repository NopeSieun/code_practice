import sys
n = int(sys.stdin.readline())

list_ = []
for i in range(n):
    list_.append(list(map(int, sys.stdin.readline().split())))
list_.sort(key=lambda x: (x[0], x[1]))
for j in list_:
    print(j[0], j[1])