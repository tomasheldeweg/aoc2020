import re
valid_rules = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (150 <= int(x[:-2]) <= 193) \
                     if x[-2:] == 'cm' else \
                     (59 <= int(x[:-2]) <= 76),
    'hcl': lambda x: bool(re.search(r'^#[0-9a-f]{6}$', x)),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: bool(re.search(r'^\d{9}$', x))
}

def count_valid_passports(filename, solution=1):
    with open(filename, 'r') as f:
        data = f.read().split('\n\n')
    count = 0

    for l in data:
        identifiers = re.findall(r'(\S{3}):(.*?)(?:\s|$)', l)
        identifiers = {k: v for k, v in identifiers if k != 'cid'}

        if len(identifiers) < 7:
            continue

        if solution == 1:
            count += 1
        elif all([valid_rules[k](v) for k, v in identifiers.items()]):
            count += 1
    return count
                  
# 4.1
print(count_valid_passports('day4/input.txt'))

# 4.2
print(count_valid_passports('day4/input.txt', solution=2))