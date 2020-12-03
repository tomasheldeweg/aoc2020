from operator import mul
from functools import reduce

def move_through_forest(filename, xmoves=3, ymoves=1):
    f = open(filename)
    first_line = next(f).rstrip('\n')
    line_width = len(first_line)
    trees = 0
    for y, line in enumerate(f, 1):
        if y % ymoves:
            continue
        if line[xmoves * int(y / ymoves) % line_width] == '#':
            trees += 1
    return trees

# 3.1
print(move_through_forest('day3/input.txt'))

# 3.2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(
    reduce(
        mul,
        [move_through_forest('day3/input.txt', x, y) for x, y in slopes]
    )
)
