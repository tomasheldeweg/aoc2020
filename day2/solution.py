import re
def get_valid_entries(filename, method='charcount'):
    policy_pw_generator = (re.split('-|:\s|\s', line.rstrip('\n')) for line in open(filename))
    count = 0
    for _min, _max, char, pw in policy_pw_generator:
        _min, _max = int(_min), int(_max)
        if method == 'charcount' and _min <= pw.count(char) <= _max:
            count += 1
        if method == 'position' and (bool(pw[_min - 1: _min] == char) ^ bool(pw[_max - 1: _max] == char)):
            count += 1
    return count

print(get_valid_entries('day2/input.txt'))

print(get_valid_entries('day2/input.txt', method='position'))