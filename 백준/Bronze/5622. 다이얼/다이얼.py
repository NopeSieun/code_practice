a = input()
num = []
#n숫자 당 n+1초가 걸리므로 n+1만큼 배당
for i in a:
    if i == 'A' or i == 'B' or i == 'C':
        i = 3
    elif i == 'D' or i == 'E' or i == 'F':
        i = 4
    elif i == 'G' or i == 'H' or i == 'I':
        i = 5
    elif i == 'J' or i == 'K' or i == 'L':
        i = 6
    elif i == 'M' or i == 'N' or i == 'O':
        i = 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        i = 8
    elif i == 'T' or i == 'U' or i == 'V':
        i = 9
    else:
        i = 10
    num.append(i)

print(sum(num))