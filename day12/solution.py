from math import cos, sin, radians
class Ship:

    def __init__(self, x=0, y=0, direction=0, waypoint=None):
        self.x = x
        self.y = y
        self.directions = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}
        self.direction = direction
        self.waypoint = bool(waypoint)
        if self.waypoint:
            self.wx = waypoint[0]
            self.wy = waypoint[1]

    def change_direction(self, amount):
        self.direction = (self.direction + amount / 90) % 4

    def change_direction_waypoint(self, amount):
        amount += self.direction * 90
        x = self.wx * cos(radians(amount)) + self.wy * sin(radians(amount))
        y = -self.wx * sin(radians(amount)) + self.wy * cos(radians(amount))
        self.wx = int(round(x))
        self.wy = int(round(y))

    def move(self, order, amount):
        if order == 'F':
            order = self.directions[self.direction]
        if order == 'N':
            self.y += amount
        elif order == 'S':
            self.y -= amount
        elif order == 'E':
            self.x += amount
        elif order == 'W':
            self.x -= amount
    
    def move_waypoint(self, order, amount):
        if order == 'F':
            self.move('E', amount * self.wx)
            self.move('N', amount * self.wy)
        elif order == 'N':
            self.wy += amount
        elif order == 'S':
            self.wy -= amount
        elif order == 'E':
            self.wx += amount
        elif order == 'W':
            self.wx -= amount

    def read_instructions(self, instructions):
        for operation in instructions:
            order, amount = operation[0], int(operation[1:])
            print(self)
            print(operation)
            if self.waypoint:
                if order == 'L':
                    self.change_direction_waypoint(-amount)
                elif order == 'R':
                    self.change_direction_waypoint(amount)
                else:
                    self.move_waypoint(order, amount)
            else:
                if order == 'L':
                    self.change_direction(-amount)
                elif order == 'R':
                    self.change_direction(amount)
                else:
                    self.move(order, amount)
        
    def __str__(self):
        return f"Ship at ({self.x}, {self.y}) heading {self.directions[self.direction]}" \
            + (f'\nWaypoint at ({self.wx}, {self.wy})' if self.waypoint else '')

    def get_manhattan_distance(self):
        return abs(self.x) + abs(self.y)


with open('day12/input.txt') as f:
    instructions = f.read().split('\n')

ship = Ship()
ship.read_instructions(instructions)
print(ship)
print('Manhatten distance:', ship.get_manhattan_distance())

ship2 = Ship(waypoint=(10, 1))
ship2.read_instructions(instructions)
print(ship2)
print('Manhatten distance:', ship2.get_manhattan_distance())