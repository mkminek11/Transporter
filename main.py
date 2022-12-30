from lib import *

g = Grid(100, 100)
cam = Camera()

@Window.w.event
def on_draw():
    Window.w.clear()
    cam.draw()

@Window.w.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    cam.move(dx, dy)

pyglet.app.run()