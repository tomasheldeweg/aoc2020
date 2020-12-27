from collections import Counter
from operator import itemgetter
with open('day17/input.txt') as f:
    con_space_slice = f.read().split('\n')

class ConwaySpace3D():

    def __init__(self, con_space_slice):
        self.cubes = []
        for y, row in enumerate(con_space_slice):
            for x, val in enumerate(row):
                if val == '#':
                    self.cubes.append((x, y, 0))

    def next(self, step=1):
        for _ in range(step):
            new_cubes = []
            position_to_active_number_map = Counter()
            for X, Y, Z in self.cubes:
                position_to_active_number_map += Counter(
                    [(x,y,z) \
                     for x in range(X - 1, X + 2) \
                     for y in range(Y - 1, Y + 2) \
                     for z in range(Z - 1, Z + 2) \
                     if not (x, y, z) == (X, Y, Z)]
                )

            for cube in self.cubes:
                if position_to_active_number_map[cube] == 2:
                    new_cubes.append(cube)

            for position, active_neighbours in position_to_active_number_map.items():
                if active_neighbours == 3:
                    new_cubes.append(position)
            self.cubes = new_cubes

    def __str__(self):
        x_min, x_max = min(self.cubes, key=itemgetter(0))[0], max(self.cubes, key=itemgetter(0))[0]
        y_min, y_max = min(self.cubes, key=itemgetter(1))[1], max(self.cubes, key=itemgetter(1))[1]
        z_min, z_max = min(self.cubes, key=itemgetter(2))[2], max(self.cubes, key=itemgetter(2))[2]
        total_str = ''
        for z in range(z_min, z_max + 1):

            slice_print = f'z={z}\n'
            for y in range(y_min, y_max + 1):

                line_print = ''
                for x in range(x_min, x_max + 1):
                    if (x, y, z) in self.cubes:
                        line_print += '#'
                    else:
                        line_print += '.'

                slice_print += line_print + '\n'
            total_str += slice_print + '\n'

        return total_str

    def count_active(self):
        return len(self.cubes)


class ConwaySpace4D():

    def __init__(self, con_space_slice):
        self.cubes = []
        for y, row in enumerate(con_space_slice):
            for x, val in enumerate(row):
                if val == '#':
                    self.cubes.append((x, y, 0, 0))

    def next(self, step=1):
        for _ in range(step):
            new_cubes = []
            position_to_active_number_map = Counter()
            for X, Y, Z, W in self.cubes:
                position_to_active_number_map += Counter(
                    [(x,y,z,w) \
                     for x in range(X - 1, X + 2) \
                     for y in range(Y - 1, Y + 2) \
                     for z in range(Z - 1, Z + 2) \
                     for w in range(W - 1, W + 2) \
                     if not (x, y, z, w) == (X, Y, Z, W)]
                )

            for cube in self.cubes:
                if position_to_active_number_map[cube] == 2:
                    new_cubes.append(cube)

            for position, active_neighbours in position_to_active_number_map.items():
                if active_neighbours == 3:
                    new_cubes.append(position)
            self.cubes = new_cubes

    def __str__(self):
        x_min, x_max = min(self.cubes, key=itemgetter(0))[0], max(self.cubes, key=itemgetter(0))[0]
        y_min, y_max = min(self.cubes, key=itemgetter(1))[1], max(self.cubes, key=itemgetter(1))[1]
        z_min, z_max = min(self.cubes, key=itemgetter(2))[2], max(self.cubes, key=itemgetter(2))[2]
        w_min, w_max = min(self.cubes, key=itemgetter(3))[3], max(self.cubes, key=itemgetter(3))[3]
        total_str = ''
        for w in range(w_min, w_max + 1):
            for z in range(z_min, z_max + 1):

                slice_print = f'z={z}, w={w}\n'
                for y in range(y_min, y_max + 1):

                    line_print = ''
                    for x in range(x_min, x_max + 1):
                        if (x, y, z, w) in self.cubes:
                            line_print += '#'
                        else:
                            line_print += '.'

                    slice_print += line_print + '\n'
                total_str += slice_print + '\n'

        return total_str

    def count_active(self):
        return len(self.cubes)

# Solve 1
space = ConwaySpace3D(con_space_slice)
for _ in range(6):
    space.next()
    print(space)
print(space.count_active())

# Solve 2
space = ConwaySpace4D(con_space_slice)
for _ in range(6):
    space.next()
    print(space)
print(space.count_active())
