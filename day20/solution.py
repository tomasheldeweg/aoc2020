import re
from pprint import pprint
from functools import reduce
from operator import mul

with open('day20/input.txt') as f:
    tiles = f.read().split('\n\n')

class Tile():

    def __init__(self, tile, header=True):
        self.id = int(re.search('\d+', tile)[0])
        self.frame = tile.split('\n')[1:]
        self.dim = len(self.frame)
        self.find_clockwise_connection_points(self.frame)

    def find_clockwise_connection_points(self, frame):
        self.edge_points = {}
        self.edge_points['top'] = tuple(i for i, x in enumerate(self.frame[0]) if x == '#')
        self.edge_points['right'] = tuple(i for i, x in enumerate([c[-1] for c in self.frame]) if x == '#')
        self.edge_points['bottom'] = tuple(i for i, x in enumerate(self.frame[-1][::-1]) if x == '#')
        self.edge_points['left'] = tuple(i for i, x in enumerate([c[0] for c in self.frame][::-1]) if x == '#')

    def flipped(self, axis=0):
        if axis == 0:
            flip_frame = [line[::-1] for line in self.frame]
        elif axis == 1:
            flip_frame = self.frame[::-1]
        header = str(self.id) + '\n'
        tile_string = header + '\n'.join(flip_frame)
        return Tile(tile_string)

    def can_connect_to(self, other):
        return bool(set(self.edge_points.values()) & set(other.edge_points.values()))

    def __str__(self):
        return str(self.id) + '\n' + \
        '\n'.join(self.frame) + '\n' + \
        '\n'.join([k + ': ' + str(v) for k, v in self.edge_points.items()]) + '\n'

    def __eq__(self, other):
        return self.id == other.id

class Picture():

    def __init__(self, tiles):
        self.tileset = tiles

    def find_connections(self):
        id_connections = {}
        for tile in self.tileset:
            id_connections[tile.id] = sum([
                tile.can_connect_to(other_tile) or \
                tile.can_connect_to(other_tile.flipped()) \
                for other_tile in self.tileset if tile != other_tile
            ])
        return id_connections


p = Picture([Tile(t.strip('\n')) for t in tiles if t])

# Solve 1
connections = p.find_connections()
corners = (id_ for id_, nr in connections.items() if nr == 2)
print(reduce(mul, corners))

# Solve 2
