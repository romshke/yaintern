sizes = [int(_) for _ in input().split()]
x, y = int(), int()

# print(max(min(sizes[:2]), min(sizes[2:])), max(sizes[:2]) + min(sizes[2:]))

x = max(min(sizes[:2]), min(sizes[2:]))

if x in sizes[:2]:
    if all(x > _ for _ in sizes[2:]):
        y = min(sizes[2:]) + max(sizes[:2])
    else:
        y = max(sizes[2:]) + max(sizes[:2])
elif x in sizes[2:]:
    if all(x > _ for _ in sizes[:2]):
        y = min(sizes[:2]) + max(sizes[2:])
    else:
        y = max(sizes[:2]) + max(sizes[2:])

print(x, y)