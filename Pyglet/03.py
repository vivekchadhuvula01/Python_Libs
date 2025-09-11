import pyglet
from pyglet.window import key

window = pyglet.window.Window()

# @window.event
# def on_key_press(symbol,modifiers):
#     print("A key was pressed")

@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.A:
        print("A is pressed")
    elif symbol == key.LEFT:
        print('Left is clicked')
    elif symbol == key.ENTER:
        print("Enter is pressed")
    
@window.event
def on_draw():
    window.clear()
    
pyglet.app.run()