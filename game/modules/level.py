from pyglet.window import key
import pyglet

import screen, resources

class LevelAdministrator(screen.Screen):
    def __init__(self, game):
        super(LevelAdministrator, self).__init__(game)
        self.game = game
        self.foreground = pyglet.graphics.OrderedGroup(1)
        self.background = pyglet.graphics.OrderedGroup(0)
        
    def on_key_press(self, symbol, modifiers):
        pass            

    def start(self):
        self.batch = pyglet.graphics.Batch()
        self.terrain = []
        poly_vertices = (50, 500, 250, 400, -50, -100)
        self.test_poly = self.batch.add(3, pyglet.gl.GL_TRIANGLES, self.foreground,
                                        ('v2f/stream', poly_vertices),
                                        ('c3B', (50, 50, 255, 50, 50, 255,
                                                 50, 50, 255))
                                        )                                  
        print "GO"

    def on_draw(self):
        super(LevelAdministrator, self).on_draw()
        self.game.window.clear()
        self.batch.draw()
        

    def clear(self):
        pass
        
    def update(self, dt):
        return
