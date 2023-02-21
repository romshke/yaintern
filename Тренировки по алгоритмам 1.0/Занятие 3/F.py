genome1, genome2, pairs = input(), set(), str()

# for _ in input():
#     if pairs == '':  
#         pairs += _
#     else:
#         pairs += _
#         # print(pairs, pairs[1:])
#         genome1.append(pairs)
#         pairs = pairs[1:]

# pairs = ''
  
for _ in input():
    if pairs == '':  
        pairs += _
    else:
        if pairs + _ not in genome2:
            pairs += _
            # print(pairs, pairs[1:])
            genome2.add(pairs)
            pairs = pairs[1:]
        else:
            pairs = _

print(sum(1 for _ in range(len(genome1) - 1) if genome1[_:_ + 2] in genome2))