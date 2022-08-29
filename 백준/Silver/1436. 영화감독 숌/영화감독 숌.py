n = int(input())
cnt = 0
new = 666
while True:
    if '666' in str(new):
        cnt += 1
    if cnt == n:
        print(new)
        break
    new += 1