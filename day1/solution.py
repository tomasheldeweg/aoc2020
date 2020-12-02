import itertools
from operator import mul
from functools import reduce

def find_number_comb(filename, n=2, total=2020):
    for comb in itertools.combinations([int(row) for row in open(filename)], n):
        if sum(comb) == total:
            return reduce(mul, comb), comb

# Solve 1.1
print(find_number_comb('day1/input.txt'))

# Solve 1.2
print(find_number_comb('day1/input.txt', n=3))