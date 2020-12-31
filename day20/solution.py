import re
from pprint import pprint
from itertools import combinations
from functools import reduce
from operator import mul

with open('day20/test_input.txt') as f:
    tiles = f.read().split('\n\n')

class Tile():

    def __init__(self, tile, header=True):
        self.id = int(re.search(r'-?\d+', tile)[0])
        self.frame = tile.split('\n')[1:]
        self.dim = len(self.frame)
        self.find_clockwise_connection_points(self.frame)

    def find_clockwise_connection_points(self, frame):
        self.edge_points = {}
        self.edge_points[0] = tuple(i for i, x in enumerate([c[-1] for c in self.frame]) if x == '#')  # RIGHT
        self.edge_points[1] = tuple(i for i, x in enumerate(self.frame[-1][::-1]) if x == '#')  # BOTTOM
        self.edge_points[2] = tuple(i for i, x in enumerate([c[0] for c in self.frame][::-1]) if x == '#')  # LEFT
        self.edge_points[3] = tuple(i for i, x in enumerate(self.frame[0]) if x == '#')  # TOP

    def flipped(self, axis=0):
        if axis == 0:
            flip_frame = [line[::-1] for line in self.frame]
        elif axis == 1:
            flip_frame = self.frame[::-1]
        header = str(-self.id) + '\n'
        tile_string = header + '\n'.join(flip_frame)
        return Tile(tile_string)

    def rotate(self, n=1, clockwise=True):
        if not clockwise:
            n = -n % 4
        else:
            n = n % 4

        rotated_frame = self.frame
        for _ in range(n):
            rotated_frame = [''.join(x) for x in zip(*rotated_frame[::-1])]

        header = str(self.id) + '\n'
        tile_string = header + '\n'.join(rotated_frame)
        return Tile(tile_string)

    def can_connect_to(self, other):
        for o in [other, other.flipped()]:
            for edge, points in self.edge_points.items():
                for o_edge, o_points in o.edge_points.items():
                    if points == tuple(o.dim - 1 - x for x in o_points[::-1]):
                        return {edge: o.rotate((edge - o_edge + 2) % 4)}
        return None

    def __str__(self):
        return str(self.id) + '\n' + \
        '\n'.join(self.frame) + '\n' + \
        '\n'.join([str(k) + ': ' + str(v) for k, v in self.edge_points.items()]) + '\n'

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other
    
    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return str(self.id)


class Picture():
    position_map = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    
    def __init__(self, tiles):
        self.tileset = tiles
        self.tile_map = self.find_tile_map()
        self.picture = self.construct_picture()
        self.dim = len(self.picture)

    def find_tile_map(self):
        """Create a dictionary of tiles: coordinates by evaluating
        the neighbours of each tile one by one and adding those to the map.
        """
        # Initial tile
        t = self.tileset[0]
        tiles_to_find_neighbours = [t]
        tile_map = {t: (0, 0)}

        while tiles_to_find_neighbours:
            tile = tiles_to_find_neighbours[0]

            # Find the edge: neighbours tiles mapping for tile above
            # Edge tile struct {original_tile_edge: neighbouring_tile}
            edge_tiles = {}
            for other_tile in self.tileset[1:]:
                if abs(tile.id) != abs(other_tile.id):
                    if con := tile.can_connect_to(other_tile):
                        edge_tiles.update(con)
                    if len(edge_tiles) > 4:
                        break
            
            # Determine if an entry has already been added to the tile map. If so, the entry
            # has already been put in the tiles_to_find_neighbour list and doesn't have to be reconsidered.
            for edge, nt in edge_tiles.items():
                if nt not in tile_map:
                    tiles_to_find_neighbours.append(nt)
                    current_coord = tile_map[tile]
                    relative_nt_coord = Picture.position_map[edge]
                    tile_map[nt] = tuple(sum(x) for x in zip(current_coord, relative_nt_coord))

            # After tile neighobours have been evaluated, remove tile from list
            tiles_to_find_neighbours.remove(tile)
        return tile_map
    
    def construct_picture(self):
        """Construct the picture frame by evaluating the range of coordinates in the tile map.
        These ranges will then be used to construct each horizontal line in the picture one by one
        """
        x_range, y_range = [sorted(set(x)) for x in zip(*self.tile_map.values())]
        coordinate_map = {coord: tile for tile, coord in self.tile_map.items()}
        picture = []
        for y in y_range:
            tile_frames = [coordinate_map[(x, y)].frame for x in x_range]
            # Strip edges with 1:-1 slices
            print([line[1:-1] for line in tile_frames[0][1:-1]])
            break
            picture += [hlines for hlines in zip(*[frame[1:-1][1:-1] for frame in tile_frames])][1:-1]
        return picture

    def rotate(self, n=1, clockwise=True):
        if not clockwise:
            n = -n % 4
        else:
            n = n % 4

        for _ in range(n):
            self.picture = [''.join(x) for x in zip(*self.picture[::-1])]
        return self

    def flip(self, axis=0):
        if axis == 0:
            self.picture = [line[::-1] for line in self.picture]
        elif axis == 1:
            self.picture = self.picture[::-1]
        return self

    def find_monster(self, monster):
        monster_height = len(monster)
        monster_width = len(monster[0])
        monster_coords = []
        for y in range(monster_height):
            for x in range(monster_width):
                if monster[y][x] == '#':
                    monster_coords.append((x, y))

        # Loop over each orientation of picture

        for flips in range(2):
            for rotations in range(4):
                # Loop over picture
                monster_found = False
                for y in range(self.dim - monster_height - 2):
                    for x in range(self.dim - monster_width - 2):
                        coords = [(x_monster + x, y_monster + y) for x_monster, y_monster in monster_coords]
                        if monster_found := any(self.picture[y][x] == '#' for x, y in coords):
                            for x, y in coords:
                                self.picture[y] = self.picture[y][:x] + 'O' + self.picture[y][x + 1:]

                if monster_found:
                    return self   
         
                self.rotate()
            self.flip()

    def __str__(self):
        return "\n".join(line for line in self.picture)





p = Picture([Tile(t.strip('\n')) for t in tiles if t])
print(p.rotate().flip())
print(p.dim)
sea_monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]
#print(p.find_monster(sea_monster))
