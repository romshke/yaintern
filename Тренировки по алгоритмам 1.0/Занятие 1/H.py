# поезд стоит на платформе 1 минуту затем в интервале a, b минут поезда нет

# @_@_@
# @___@

# _@_@_@_
# __@___@

a, b, n, m = int(input()), int(input()), int(input()), int(input())

fst_train = [n + (n - 1) * a, n + (n + 1) * a]
snd_train = [m + (m - 1) * b, m + (m + 1) * b]

if max(fst_train) >= min(snd_train) and min(fst_train) <= max(snd_train): print(max(min(fst_train), min(snd_train)), min(max(fst_train), max(snd_train)))
else: print(-1)
