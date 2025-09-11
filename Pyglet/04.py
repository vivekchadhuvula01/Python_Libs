import pyglet 
from pyglet.window import mouse

window = pyglet.window.Window()

@window.event
def on_mouse_press(x,y,button,modifiers):
    if button == mouse.LEFT:
        print("Left")
    elif button == mouse.MIDDLE:
        print("Middle")
    elif button == mouse.RIGHT:
        print("Right")
        
        
pyglet.app.run()