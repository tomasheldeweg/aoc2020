"""
No mem solve with chained generators
"""
def find_number_pair(filename, total=2020):
    with open(filename) as f:
        for i, line in enumerate(f):
            with open(filename) as f2:
                for j, line2 in enumerate(f2):
                    with open(filename) as f3:
                        for k, line3 in enumerate(f3):
                            if int(line) + int(line2) + int(line3) == total and len(set([i, j, k])) == 3:
                                return int(line) * int(line2) * int(line3)
print(find_number_pair('day2/input.txt'))
