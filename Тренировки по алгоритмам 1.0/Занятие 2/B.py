constant, ascending, weakly_ascending, descending, weakly_descending = True, True, True, True, True
number = int()
previous = None

while True:
    number = int(input())
    
    if number == -2 * 10**9: break
    
    if previous is not None:
        if number != previous: constant = False
        elif number == previous: 
            # print(ascending, descending)
            if ascending:
                weakly_descending = False
                ascending = False 
            if descending:
                weakly_ascending = False
                descending = False
        if number < previous:
            ascending = False
            weakly_ascending = False
            # print(ascending, weakly_ascending)
            # if number == previous: descending = False
        if number > previous:
            descending = False
            weakly_descending = False
            # print(descending, weakly_descending)
            # if number == previous: ascending = False
    
    previous = number

if constant: print('CONSTANT')    
elif ascending:
    weakly_ascending = False
    print('ASCENDING')
elif weakly_ascending:
    print('WEAKLY ASCENDING')
elif descending:
    weakly_descending = False
    print('DESCENDING')
elif weakly_descending:
    print('WEAKLY DESCENDING')
# elif all((constant, ascending, weakly_ascending, descending, weakly_descending)) == False: print('RANDOM')

            
print(constant, ascending, weakly_ascending, descending, weakly_descending)

# print(all((constant, ascending, weakly_ascending, descending, weakly_descending)) == False)


# 1
# 1
# 1
# 2
# -2000000000
# RANDOM