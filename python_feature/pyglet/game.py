#!/usr/bin/env python
#Date:2018/5/28
#Author:dylan_xi
#Desc:learn python game framework
from pyglet.gl import *
import pyglet
window = None
try:
    # Try and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)
window.set_caption('test_game by dylan_xi')

pyglet.clock.set_fps_limit(60)
fps_display = pyglet.clock.ClockDisplay(format = "fps:%(fps).2f")
pyglet.clock
@window.event
def on_draw():
    window.clear()
    fps_display.draw()


if __name__ == '__main__':
    pyglet.app.run()