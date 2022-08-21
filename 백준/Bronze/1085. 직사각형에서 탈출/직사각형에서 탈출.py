n = list(map(int,input().split()))

left = n[0]
right = n[2] - n[0]
up = n[3] - n[1]
down = n[1]

d = []
d.append(left)
d.append(right)
d.append(up)
d.append(down)

print(min(d))
