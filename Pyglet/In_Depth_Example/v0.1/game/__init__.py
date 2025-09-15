import pyglet

game_window = pyglet.window.Window(800,600)
# pyglet.resource.path= ['../resources']
# pyglet.resource.reindex()

player_image =  pyglet.resource.image('resources/player.png')
bullet_image = pyglet.resource.image('bullet.png')
asteriod_image = pyglet.resource.image('asteriod.png')

if __name__ == '__main__':
    pyglet.app.run()