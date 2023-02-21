result = set()
n = int(input())

for _ in range(n):
    statement = input()
    numbers = map(int, statement.split())
    if sum(numbers) == n - 1 and all(_ >= 0 for _ in numbers):
        result.add(statement)
        
print(len(result))