n, k, m = map(int, input().split())

# result = (n // k) * (k // m)
# n -= result * m
# # print(result, n)

# while n // k > 0:
#     details = (n // k) * (k // m)
#     result += details
#     n -= details * m
#     # print(result, n)

q = k // m
m *= q

print(((n - k + 1) // m + bool((n - k + 1) % m)) * q)