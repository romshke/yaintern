a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

brick = sorted([a, b, c])
flag = False

for i in range(3):
    if brick[i] <= d:
        for j in range(3):
            if i == j: continue
            elif brick[j] <= e: flag = True

print('YES' if flag else 'NO') 