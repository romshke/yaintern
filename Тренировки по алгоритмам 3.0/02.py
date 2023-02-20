indexes = dict()
k = int(input())

for index, value in enumerate(input()):
    if value not in indexes:
        indexes.setdefault(value, [index,])
    else:
        indexes[value].append(index)

# for _ in indexes.values()

for _ in indexes.values():
    if len(_) > 1:
        print(_)

