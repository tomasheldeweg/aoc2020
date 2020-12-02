"""
No mem solve
"""
def find_number_pair(filename='input.txt', total=2020):
    with open(filename) as f:
        for i, line in enumerate(f):
            with open(filename) as f2:
                for j, line2 in enumerate(f2):
                    if int(line) + int(line2) == total and i != j:
                        return int(line) * int(line2)
print(find_number_pair('input.txt'))
