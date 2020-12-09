from pprint import pprint
import re
filename = 'day7/input.txt'


# Obtain data
nested_bags = {}
for bag_info in open(filename):
    key_bag, inner_bags = bag_info.split(' bags contain')
    bag_info = {bag: int(nr) for nr, bag in re.findall(r'(\d) (\w+ \w+)', inner_bags)}
    nested_bags[key_bag] = bag_info

# Recursive function that returns True when it finds the bag
def recurse(bag=None):
    if 'shiny gold' in nested_bags[bag]:
        return True
    for k in (nested_bags[bag] if bag else nested_bags):
        if isinstance(nested_bags[k], dict):
            if (has_bag := recurse(k)):
                return has_bag

# Solve 1
count = 0
for bag in nested_bags:
    if recurse(bag):
        count += 1
print(count)


# Recursive function that yields counts of bags in shiny bag
def recurse2(bag=None, nr=1):
    for k, v in nested_bags[bag].items():
        yield v * nr
        if isinstance(nested_bags[k], dict) and nested_bags[k]:
            yield from recurse2(k, nr=nr*v)

# Solve 2
print(sum([x for x in recurse2('shiny gold')]))