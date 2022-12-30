from lib.grid import Grid

class Camera:
    x_shift = 0
    y_shift = 0
    scale = 1

    def __init__(self):
        pass

    def draw(self):
        for y in Grid.G:
            for x in y:
                x.sprite.draw()