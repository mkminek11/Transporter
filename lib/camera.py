from lib.grid import Grid, Tile
from lib.window import Window

class Camera:
    x_shift = 0
    y_shift = 0
    scale = 1

    def __init__(self):
        pass

    def draw(self):
        Grid.batch.draw()
        for y, row in enumerate(Grid.G):
            for x, cell in enumerate(row):
                dx = x * 64 + Camera.x_shift
                dy = y * 64 + Camera.y_shift
                if dx < Window.w.width and dy < Window.w.height and dx > -64 and dy > -64:
                    cell.sprite.visible = True
                    self._update_position(cell)
                else:
                    cell.sprite.visible = False

    def move(self, dx, dy):
        Camera.x_shift += dx
        Camera.y_shift += dy

    def _update_position(self, cell:Tile):
        cell.sprite.x = 64 * cell.x + Camera.x_shift
        cell.sprite.y = 64 * cell.y + Camera.y_shift