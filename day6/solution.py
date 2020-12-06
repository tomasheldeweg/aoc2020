from functools import reduce
def count_valid_passports(filename, solution='6.1'):
    with open(filename, 'r') as f:
        data = f.read().split('\n\n')

    return (
        sum(len(set(x.replace('\n', ''))) for x in data)
        if solution == '6.1' else
        sum(len(reduce(lambda x,y: set(x) & set(y), filter(None, x.split('\n')))) for x in data)
    )

# 6.1
print(count_valid_passports('day6/input.txt'))

# 6.2
print(count_valid_passports('day6/input.txt', solution='6.2'))

