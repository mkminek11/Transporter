import pyglet, pickle
from random import choice
import lib.data as Data


class Tile:
    def __init__(self, num:int, x:int, y:int):
        self.num = num
        self.text = Data.TILE_NAMES[num]
        self.sprite = pyglet.sprite.Sprite(Data.TILE_IMAGES[num], batch=Grid.batch)
        self.x = x
        self.y = y
        self.sprite.x = Data.TILE_SIZE * x
        self.sprite.y = Data.TILE_SIZE * y


class Grid:
    G:list[list[Tile]] = []
    batch = pyglet.graphics.Batch()
    
    def __init__(self, width:int=0, height:int=0):
        self.height = Data.GRID_HEIGHT = height
        self.width  = Data.GRID_WIDTH  = width
        Grid.G = self.generate_randomly()

    def generate_randomly(self):
        result:list[list[Tile]] = []
        for y in range(self.height):
            result.append([])
            for x in range(self.width):
                tile_id = self._generate_single_tile(self._return_if_exists(result, x-1, y), self._return_if_exists(result, x, y-1))
                result[y].append(Tile(tile_id, x, y))
        return result

    def _return_if_exists(self, lst:list, x:int, y:int):
        if not (x >= 0 and y >= 0):
            return None
        try:
            return lst[y][x].text
        except:
            return None

    def _generate_single_tile(self, x1val, y1val):
        """
        x1val: value of tile with position x = x-1 and y = y
        y1val: value of tile with position x = x and y = y-1
        """
        available = list(range(len(Data.TILE_NAMES)))
        done = False
        while not done:
            chosen_nr = choice(available)
            chosen = Data.TILE_NAMES[chosen_nr]
            if (not x1val or (x1val[1] + x1val[2] == chosen[0] + chosen[3])) and (not y1val or (y1val[0] + y1val[1] == chosen[3] + chosen[2])):
                return chosen_nr
            else:
                available.remove(chosen_nr)

    def generate_by_seed(self, seed):
        pass

    def generate_from_file(self, path):     # may create not matching map from ´fake´ file
        pass

    def export_data(self):
        g = [[cell.num for cell in row] for row in Grid.G]
        with open("save.dat", "wb") as fout:
            pickle.dump(g, fout)
        print("Export successful!")

    def import_data(self):
        with open("save.dat", "rb") as fin:
            a = pickle.load(fin)
            print("Import successful!")
        Grid.G = [[Tile(cell, x, y) for x, cell in enumerate(row)] for y, row in enumerate(a)]