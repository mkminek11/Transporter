import pyglet

TILE_NAMES  = ["WWWW", "WWGW", "WWGG", "WGGG", "GGGG", "GWWW", "GGWW", "WGWW", "WGGW", "GGGW", "GWGG", "GGWG", "WWWG", "GWWG"]
TILE_IMAGES = list(pyglet.image.ImageGrid(pyglet.image.load("img/ground.png"), 2, 7))

TILE_SIZE = 64 # with no scale

GRID_WIDTH  = 10
GRID_HEIGHT = 10