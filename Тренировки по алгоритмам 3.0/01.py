all_symbols = []

with open('Тренировки по алгоритмам 3.0\Дивизион A\input.txt') as file:
    all_symbols = [_ for _ in file.read() if _ not in ' \n']

unique_symbols = set(all_symbols)

# print(all_symbols, sorted(unique_symbols, key=ord))

rows_count = [list(all_symbols).count(_) for _ in sorted(unique_symbols, key=ord)]

max_row = max(rows_count)

for i in range(max_row):
    for j in range(len(rows_count)):
        if max_row - rows_count[j] >= i + 1: print(' ', end='')
        else: print('#', end='')
    print()
    
print(*sorted(unique_symbols, key=ord), sep='')
