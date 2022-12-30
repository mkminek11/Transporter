from lib import *

g = Grid(10, 10)
c = Camera()

@Window.w.event
def on_draw():
    Window.w.clear()
    c.draw()


pyglet.app.run()