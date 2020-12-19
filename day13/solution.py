from itertools import count
from functools import reduce
from operator import mul
with open('day13/input.txt') as f:
    info = f.read().split('\n')

current_time = int(info[0])

# Solve 1
busses = [int(x) for x in info[1].split(',') if x != 'x']
nearest_times = {bus: bus - current_time % bus for bus in busses}
closest_bus = min(nearest_times.items(), key=lambda x: x[1])

print(f"Closest bus: {closest_bus[0]}\nWait time {closest_bus[1]}\nSolution = {closest_bus[0] * closest_bus[1]}")

# Solve 2
busses = {int(x): minutes for minutes, x in enumerate(info[1].split(',')) if x != 'x'}

# Chinese remainder:
max_product = reduce(mul, busses.keys())

total = 0
for divisor, remainder in busses.items():
    N = int(max_product/divisor)
    for x in count():
        if (x * N) % divisor == 1:
            break
    total += remainder * N * x

print(max_product - total % max_product)
