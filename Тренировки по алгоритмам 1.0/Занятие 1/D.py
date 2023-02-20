a, b, c = int(input()), int(input()), int(input())

if a != 0 and c >= 0:
    if ((c**2 - b) % a == 0): print((c**2 - b) // a)
    else: print('NO SOLUTION')
elif (c < 0): print('NO SOLUTION')
elif (a == 0):
    if (b >= 0 and b**0.5 == c): print('MANY SOLUTIONS')
    else: print('NO SOLUTION')