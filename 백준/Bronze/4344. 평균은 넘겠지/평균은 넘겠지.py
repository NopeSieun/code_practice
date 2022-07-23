n = int(input())

for i in range(n):
    score = list(map(int, input().split()))
    aver = sum(score[1:])/score[0]
    c = 0
    for i in score[1:]:
        if i > aver:
            c += 1
    rate = c/score[0]*100 
    print(f'{rate:.3f}%')
    #round() 썼더니 출력값이 40.000%가 아니라 40.0%로 떠서 오답이 됨