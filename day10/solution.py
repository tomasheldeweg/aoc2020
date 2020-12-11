from functools import reduce
from itertools import groupby
from operator import mul
data = sorted(int(x) for x in open('day10/input.txt'))
first = 0
diffs = [-first + (first := x) for x in data]

# Solve 1
print((diffs.count(3) + 1) * (diffs.count(1) + 1))

"""
1: 1
1 3

2: 2
1 1 3
2   3

3: 4
1 1 1 3
1 2   3
2   1 3
3     3

4: 7
1 1 1 1 3
1 1 2   3
1 2   1 3
1 3     3
2   1 1 3
2   2   3
3     1 3

5: 13
1 1 1 1 1 3
1 1 1 2   3
1 1 3     3
1 1 2   1 3
1 2   1 1 3
1 2   2   3
1 3     1 3
2   1 1 1 3
2   1 2   3
2   2   1 3
2   3     3
3     1 1 3
3     2   3

1, 2, 4, 7, 13 -> f(x) = f(x - 1) + f(x - 2) + f(x - 3)

"""
def f(x):
    if x == 1:
        return 0
    elif x == 2:
        return 0
    elif x == 3:
        return 1
    return f(x - 1) + f(x - 2) + f(x - 3)

# Solve 2
grouped_ones = [sum(1 for nr in group) for nr, group in groupby(diffs) if nr == 1]
print(reduce(mul, [f(x + 3) for x in grouped_ones]))
