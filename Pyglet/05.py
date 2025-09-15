import pyglet

media = pyglet.media,locals()
# print(media[-1])
'''
As with the image loading example presented earlier, media() locates the sound file in the application’s directory (not the working directory). If you know the actual filesystem path (either relative or absolute), use pyglet.media.load().
'''

music = pyglet.resource.media('music.mp3')

music.play()

pyglet.app.run()


'''
By default, audio is streamed when playing. This works well for longer music tracks. Short sounds, such as a gunfire shot used in a game, should instead be fully decoded in memory before they are used. This allows them to play more immediately and incur less of a CPU performance penalty. It also allows playing the same sound repeatedly without reloading it. Specify streaming=False in this case:
'''