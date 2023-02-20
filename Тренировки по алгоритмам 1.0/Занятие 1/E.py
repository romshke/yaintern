import math

K1, M, K2, P2, N2 = map(int, input().split())

# K2 // N2 - количество квартир на этаже
# K2 // N2 * M - количество квартир в подъезде
# K1 // (K2 // N2 * M) + 1 - номер подъезда, если P2 = 1

NK = math.ceil(K2 / N2)

if (P2 == 1):
    print(K1 // (NK * M) + 1, math.ceil(K1 % (NK * M) / NK))
else:
    print()
