from itertools import combinations, islice
from collections import deque

def find_invalid_number(preamble=25):
    f = open('day9/input.txt')

    number_set = deque(int(x) for x in islice(f, preamble))
    nr = int(next(f))
    while any(sum(comb) == nr for comb in combinations(number_set, 2)):
        number_set.append(nr)
        number_set.popleft()
        nr = int(next(f))
    return nr

def find_contiguous_set(total):
    for window_size in range(2, total):
        f = open('day9/input.txt')
        number_set = deque(int(x) for x in islice(f, window_size))
        while next_nr := next(f, None):
            if sum(number_set) == total:
                return min(number_set) + max(number_set)
            number_set.append(int(next_nr))
            number_set.popleft()

# Solve 1
print(total := find_invalid_number())

# Solve 2
print(find_contiguous_set(total))