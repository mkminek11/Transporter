import pyglet


class Grid:

    G = []
    
    def __init__(self, width:int=0, height:int=0, fill=None):
        
        self.G = self.generate_randomly()

    def generate_randomly(self):
        pass

    def _generate_single_tile(self, x1val, y1val):
        """
        x1val: value of tile with position x = x-1 and y = y
        y1val: value of tile with position x = x and y = y-1
        """
        pass

    def generate_by_seed(self, seed):
        pass

    def generate_from_file(self, path):     # may create not matching map with ´fake´ file
        pass