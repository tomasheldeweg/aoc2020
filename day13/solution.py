from itertools import count
with open('day13/test_input.txt') as f:
    info = f.read().split('\n')

current_time = int(info[0])

# Solve 1
busses = [int(x) for x in info[1].split(',') if x != 'x']
nearest_times = {bus: bus - current_time % bus for bus in busses}
closest_bus = min(nearest_times.items(), key=lambda x: x[1])

print(f"Closest bus: {closest_bus[0]}\nWait time {closest_bus[1]}\nSolution = {closest_bus[0] * closest_bus[1]}")

# Solve 2
busses = {int(x): minutes for minutes, x in enumerate(info[1].split(',')) if x != 'x'}
_min, _max = min(busses.keys()), max(busses.keys())
step = _min * _max
print(step)
offset_max = busses[_max]

for i in count(0, step):
    i -= offset_max
    nr_matches = 0
    for bus, offset in busses.items():
        if not (offset + i) % bus:
            nr_matches += 1
        else:
            break
    if nr_matches == len(busses):
        print(i)
        break