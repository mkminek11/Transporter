from lib.grid import Grid, Tile
from lib.window import Window
import lib.data as Data

class Camera:
    x_shift = 0
    y_shift = 0
    scale = 1

    @classmethod
    def draw(cls):
        cls.resize()
        Grid.batch.draw()

    @classmethod
    def move(cls, dx, dy):
        Camera.x_shift += dx
        Camera.y_shift += dy

    @classmethod
    def resize(cls):
        for y, row in enumerate(Grid.G):
            for x, cell in enumerate(row):
                dx = x * Data.TILE_SIZE + Camera.x_shift
                dy = y * Data.TILE_SIZE + Camera.y_shift
                if dx < Window.w.width and dy < Window.w.height and dx > -Data.TILE_SIZE and dy > -Data.TILE_SIZE:
                    cell.sprite.visible = True
                    cls._update_position(cell)
                else:
                    cell.sprite.visible = False

    @classmethod
    def _update_position(cls, cell:Tile):
        cell.sprite.x = Data.TILE_SIZE * cell.x + Camera.x_shift
        cell.sprite.y = Data.TILE_SIZE * cell.y + Camera.y_shift