n, m = map(int, input().split())
ann = set(int(input()) for _ in range(n))
boris = set(int(input()) for _ in range(m))

print(len(ann & boris))
print(*sorted(ann & boris))
print(len(ann - (ann & boris)))
print(*sorted(ann - (ann & boris)))
print(len(boris - (ann & boris)))
print(*sorted(boris - (ann & boris)))