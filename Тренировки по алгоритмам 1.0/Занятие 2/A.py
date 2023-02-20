from sys import maxsize


flag = True
previous = -maxsize
numbers = list()

for _ in input().split():
    if previous < int(_): previous = int(_)
    else: flag = False
    
print('YES' if flag else 'NO')