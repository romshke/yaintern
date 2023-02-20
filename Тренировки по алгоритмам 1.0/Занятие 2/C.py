n = int(input())
lst = map(int, input().split())
x = int(input())
difference = None
result = int()

for _ in lst:
    if difference is not None:
        if abs(_ - x) < difference:
            difference = abs(_ - x)
            result = _
    else:
        difference = abs(_ - x)
        result = _
        
    # print(_, difference)

print(result)