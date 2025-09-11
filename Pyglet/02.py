import pyglet  

window  = pyglet.window.Window()
image =  pyglet.resource.image("assets/logo.jpeg")

@window.event
def on_draw():
    window.clear()
    image.blit(0,0)     
'''
Blit the texture to the screen.
This is a costly operation, and should not be used for performance critical code. Blitting a texture requires binding it, setting up throwaway buffers, creating a VAO, uploading attribute data, and then making a single draw call. This is quite wasteful and slow, so blitting should not be used for more than a few images. This method is provided to assist with debugging, but not intended for drawing of multiple images.
'''
    
pyglet.app.run()
