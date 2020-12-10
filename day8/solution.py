import re
f = open('day8/input.txt')

data = f.read().split('\n')

def iterate_data(data, change_nop_jmp_idx=None):
    acc, idx = 0, 0
    executed_operations = set()
    max_idx = len(data) - 1
    while idx <= max_idx:
        line = data[idx]

        if str(idx) + line in executed_operations:
            return acc, idx
        else:
            executed_operations.add(str(idx) + line)

        operation, amount = line.split(' ')
        if operation == 'acc':
            acc += int(amount)
            idx += 1
        elif operation == 'nop' or (change_nop_jmp_idx == idx and operation == 'jmp'):
            idx += 1
        elif operation == 'jmp'or (change_nop_jmp_idx == idx and operation == 'nop'):
            idx += int(amount)
    return acc, idx

# Solve 8.1
print(iterate_data(data)[0])


# Solve 8.2
termination_idx = len(data)
jmp_nop_indexes = [idx for idx, op in enumerate(data) if op.startswith('jmp') or op.startswith('nop')]
for jmp_nop_idx in jmp_nop_indexes:
    acc, idx = iterate_data(data, jmp_nop_idx)
    if idx == termination_idx:
        print(acc)
        break
