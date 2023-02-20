lst = list(map(int, input().split()))
count = 0

for _ in range(1, len(lst) - 1):
    if lst[_ - 1] < lst[_] and lst[_ + 1] < lst[_]: count += 1
    
print(count)