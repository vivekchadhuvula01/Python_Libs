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
    
    
'''
There are more than 20 event types that you can handle on a window. An easy way to find the event names and parameters you need is to add the following lines to your program:
'''
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)
        
pyglet.app.run()