from copy import deepcopy
with open('day11/input.txt') as f:
    data = f.read().split('\n')
data = [[c for c in x] for x in data]
ADJACENT_CELLS = [(y, x) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == y == 0)]

class Grid():

    def __init__(self, data, method='adjacent'):
        self.data = data
        self.x_rows, self.y_rows = len(data[0]), len(data)
        self.cells = [Cell(self.data, x, y, method) for y in range(self.y_rows) for x in range(self.x_rows)]

    def transform(self):
        [cell.transform() for cell in self.cells]
        [self.update_data(cell) for cell in self.cells]
        [cell.calc_neighbouring_occupants(self.data) for cell in self.cells]

    def update_data(self, cell):
        self.data[cell.y][cell.x] = cell.value

    def get_state(self):
        total_occupied = sum(1 for cell in self.cells if cell.value == '#')
        total_empty = sum(1 for cell in self.cells if cell.value == 'L')
        return total_occupied, total_empty

    def __str__(self):
        return '\n'.join(["".join(x) for x in self.data])

class Cell():

    def __init__(self, grid, x, y, method='adjacent'):
        self.x, self.y = x, y
        self.value = grid[y][x]
        self.method = method
        self.calc_neighbouring_occupants(grid)
        if self.method == 'adjacent':
            self.occupants_limit = 4
        elif self.method == 'line_of_sight':
            self.occupants_limit = 5
        else:
            raise NotImplementedError

    def calc_neighbouring_occupants(self, grid):
        if self.value == '.':
            self.nr_adjacent_occupants = -1
            return

        count = 0
        max_x, max_y = len(grid[0]), len(grid)

        # Adjacency solve 11.1
        if self.method == 'adjacent':
            for x, y in ADJACENT_CELLS:
                if 0 <= (self.x + x) < (max_x) and \
                0 <= (self.y + y) < (max_y) and \
                grid[self.y + y][self.x + x] == '#':
                    count += 1
        elif self.method == 'line_of_sight':
            
        else:
            raise NotImplementedError
        # Line of sight solve 11.2
        self.nr_adjacent_occupants = count

    def transform(self):
        if self.value == 'L' and self.nr_adjacent_occupants == 0:
            self.value = '#'
        elif self.value == '#' and self.nr_adjacent_occupants >= self.occupants_limit:
            self.value = 'L'

    def __str__(self):
        return str(self.value)


# Solve1
data1 = deepcopy(data)
grid = Grid(data1)
prev_state = None
while (state := grid.get_state()) != prev_state:
    grid.transform()
    prev_state = state
print(grid.get_state()[0])

# Solve2
grid = Grid(data, method='line_of_sight')
prev_state = None
while (state := grid.get_state()) != prev_state:
    grid.transform()
    prev_state = state