test = int(input())
score = list(map(int,input().split()))
max_score = max(score)
newscore = []

for i in score:
    i = i/max_score*100
    newscore.append(i)

sum_ = sum(newscore)
print(sum_/len(newscore))