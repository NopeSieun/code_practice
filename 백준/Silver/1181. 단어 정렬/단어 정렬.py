n = int(input())
word_list = []

for _ in range(n):
    word_list.append(input())
newlist = list(set(word_list))
newlist.sort()
newlist.sort(key = len)

for i in newlist:
    print(i)