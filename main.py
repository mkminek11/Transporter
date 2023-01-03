from pyglet.window import key
from lib import *

g = Grid(100, 100)

@Window.w.event
def on_draw():
    Window.w.clear()
    Camera.draw()

@Window.w.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    Camera.move(dx, dy)

@Window.w.event
def on_key_press(symbol, modifiers):
    match symbol:
        case key.E:
            g.export_data()
        case key.I:
            g.import_data()

@Window.w.event
def on_resize(w, h):
    Camera.resize()

pyglet.app.run()