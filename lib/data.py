import pyglet

class Data:
    TILE_NAMES  = []
    TILES_IMAGE = list(pyglet.image.ImageGrid(pyglet.image.load("img/ground.png"), 5, 5))

    TILE_SIZE = 64 # with no scale

    GRID_WIDTH  = 10
    GRID_HEIGHT = 10