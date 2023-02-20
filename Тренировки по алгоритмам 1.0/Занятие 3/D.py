with open('input.txt') as file:
    print(len(set(file.read().split())))