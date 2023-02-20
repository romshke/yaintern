n = int(input())
cards = sorted(set(map(int, input().split())))
k = int(input())
numbers = list(map(int, input().split()))

print(n, cards, k, numbers)

for _ in numbers:
    pass