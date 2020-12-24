import re
from itertools import product
with open('day14/input.txt') as f:
    data = f.read().split('mask = ')

def memory_mapping():
    mem = {}
    for group in data:
        mask = group[:36]
        replace_indices = [(ind, c) for ind, c in enumerate(mask) if c in '10']

        for mem_loc, val in re.findall(r'mem\[(\d+)\] = (\d+)', group):
            # Make byte string 'mutable' by changing into list
            val = list(f"{int(val):036b}")

            for ind, masked_val in replace_indices:
                val[ind] = masked_val

            val = int(''.join(val), 2)
            mem[mem_loc] = val

    return mem

# Solve 1
print(sum(memory_mapping().values()))

def address_masking():
    mem = {}
    for group in data:
        mask = group[:36]
        replace_indices = [ind for ind, c in enumerate(mask) if c == '1']
        comb_indices = [ind for ind, c in enumerate(mask) if c == 'X']

        for mem_address, val in re.findall(r'mem\[(\d+)\] = (\d+)', group):
            # Make byte string 'mutable' by changing into list
            mem_address = list(f"{int(mem_address):036b}")

            for ind in replace_indices:
                mem_address[ind] = '1'

            for combination in product('10', repeat=len(comb_indices)):
                for ind, masked_char in zip(comb_indices, combination):
                    mem_address[ind] = masked_char
                mem[int(''.join(mem_address), 2)] = int(val)

            else:
                mem[int(''.join(mem_address), 2)] = int(val)
    return mem

# Solve 2
print(sum(address_masking().values()))