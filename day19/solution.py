import re
from ast import literal_eval
from pprint import pprint
with open('day19/input.txt') as f:
    rules, messages = f.read().split('\n\n')

rules = [rule.split(': ') for rule in rules.split('\n')]
rules = {key: rule for key, rule in rules}

def obtain_pattern_zero(rules):
    # Prevent recursion
    for key, val in rules.items():
    while any(char.isdigit() for char in rules['0']):
        replace = {}
        for key, val in rules.items():
            if not any(char.isdigit() for char in val):
                replace[key] = '(' + val + ')' if len(val) > 3 else val

        for rk, rv in replace.items():
            for k, v in rules.items():
                if k == rk:
                    print(k, rk, 'dupli')
                rules[k] = re.sub(
                    r'(\D|^)' + rk + r'(\D|$)',
                    r'\g<1>' + rv + r'\g<2>',
                    v
                )

    master_rule = rules['0'].replace('"', '').replace(' ', '')
    print(master_rule)
    return re.compile(master_rule)

# Solve 1
rules1 = rules.copy()
p = obtain_pattern_zero(rules1)
total = sum(bool(p.fullmatch(line)) for line in messages.split('\n'))
print(total)

# Solve 2
rules2 = rules.copy()
rules2['8'] = '42 R' # '42 | 42 8'
rules2['11'] = '42 R 31' # '42 31 | 42 11 31'

p = obtain_pattern_zero(rules2)

