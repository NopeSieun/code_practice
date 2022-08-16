while True:
    cnt = 0
    st = input()
    if st == '#':
        break
    st = list(st)
    for s in st:
        if s == 'a'or s =='e'or s =='i'or s =='o'or s =='u':
            cnt+=1
        elif s =='A' or s == 'E' or s == 'I' or s =='O' or s == 'U':
            cnt+=1
    print(cnt)        
