while True:
    st = list(input().split())
    if st[0] == '#' and st[1] == '0' and st[2] == '0':
        break
    if int(st[1])>17 or int(st[2])>=80:
        print(st[0],'Senior')
    else:
        print(st[0],'Junior')
