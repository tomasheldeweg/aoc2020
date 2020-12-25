import re
from operator import mul
from functools import reduce

with open('day16/input.txt') as f:
    rules, my_ticket, other_ticket = f.read().split('\n\n')

def rule_creator(x1, x2, y1, y2):
    return lambda x: int(x1) <= int(x) <= int(x2) or int(y1) <= int(x) <= int(y2)

rules_dict = {name: rule_creator(x1, x2, y1, y2) \
              for (name, x1, x2, y1, y2) in re.findall('(.*): (\d+)-(\d+) or (\d+)-(\d+)', rules)}

def get_valid_tickets():
    total = 0
    valid_tickets = []
    for ticket in other_ticket.split('\n')[1:]:
        for number in ticket.split(','):
            if not any(rule(number) for rule in rules_dict.values()):
                total += int(number)
                break
        else:
            valid_tickets.append(ticket)

    return total, [[int(x) for x in ticket.split(',')] for ticket in valid_tickets]

sum_invalid_tickets, valid_tickets = get_valid_tickets()

# Solve 1
print(sum_invalid_tickets)

def determine_possible_rule_field_mapping(valid_tickets):
    transpose_valid_tickets = zip(*valid_tickets)
    possible_fields = {name: set() for name in rules_dict}
    for field, position in enumerate(transpose_valid_tickets):
        for name, rule in rules_dict.items():
            if all(rule(nr) for nr in position):
                possible_fields[name].add(field)
    return dict(sorted(possible_fields.items(), key=lambda item: len(item[1])))

def solve_name_field_map(possible_fields):
    positions = set()
    unique_name_field_map = {}
    for name, fields in possible_fields.items():
        unique_field = list(positions ^ fields)[0]
        positions.add(unique_field)
        unique_name_field_map[name] = unique_field
    return unique_name_field_map

def my_ticket_departures_sum(rule_field_map, my_ticket):
    my_ticket = [int(x) for x in my_ticket.split('\n')[1].split(',')]
    return reduce(mul, (my_ticket[field] for name, field in rule_field_map.items() if name.startswith('departure')))


# Solve 2
possible_fields = determine_possible_rule_field_mapping(valid_tickets)
rule_field_map = solve_name_field_map(possible_fields)
print(my_ticket_departures_sum(rule_field_map, my_ticket))