number_2_add = ''.join([_ for _ in input() if _.isdigit()])
new_numbers = [''.join([_2 for _2 in input() if _2.isdigit()]) for _1 in range(3)]

for _ in new_numbers:
    if len(number_2_add) == 11:
        if len(_) == 11:
            print('YES' if number_2_add[1:] == _[1:] else 'NO')
        else:
            print('YES' if number_2_add[1:] == '495' + _ else 'NO')
    else:
        if len(_) == 11:
            print('YES' if '495' + number_2_add == _[1:] else 'NO')
        else:
            print('YES' if number_2_add == _ else 'NO')
        