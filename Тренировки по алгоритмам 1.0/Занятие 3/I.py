students = [set(input() for _ in range(int(input()))) for _ in range(int(input()))]

all_know = set.intersection(*students)
at_least_one_know = set.union(*students)
        
print(len(all_know), *all_know, len(at_least_one_know), *at_least_one_know, sep='\n')