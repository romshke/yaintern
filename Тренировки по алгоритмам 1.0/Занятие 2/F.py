n = int(input())
sequence = list(map(int, input().split()))

for _ in range(len(sequence)):
    if sequence[_] == sequence[-_]:
        print()
    