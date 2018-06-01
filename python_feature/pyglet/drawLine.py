#!/usr/bin/env python
#Date:2018/5/28
#Author:dylan_xi
#Desc:draw Line :根据鼠标位置画两条垂直的线段,基于屏幕中心

from pyglet.gl import *
import pyglet
import Line2
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

screenWidth , screenHeight = window.get_size()
centerSize = [0 ,0]
centerSize[0] = screenWidth/2
centerSize[1] = screenHeight/2
mousePos = [0 , 0]

drawPos1 = [0 , 0] 
drawPos2 = [0 , 0]

drawPos3 = [0 , 0] 
drawPos4 = [100 , 100]

@window.event
def on_draw():
    window.clear()
    print(drawPos1 , drawPos2 , drawPos3 , drawPos4)
    pyglet.graphics.draw(4, pyglet.gl.GL_LINES,
    ('v2f', (drawPos1[0], drawPos1[1], drawPos2[0] , drawPos2[1]
    , drawPos3[0], drawPos3[1], drawPos4[0] , drawPos4[1]))
    )

def getLineBoundaryPos(line):
    x1 = 0 
    x2 = screenWidth
    y1 = line.getY(x1)
    y2 = line.getY(x2)
    if y1 == None or y2 == None:
        y1 = 0 
        y2 = screenHeight
        x1 = line.getX(y1)
        x2 = line.getX(y2)
    return x1 , y1 , x2 , y2    

@window.event
def on_mouse_motion(x, y, dx, dy):
    mousePos[0] = x
    mousePos[1] = y
    line = Line2.Line2(centerSize[0], centerSize[1], mousePos[0] , mousePos[1])
    drawPos1[0] ,drawPos1[1] ,drawPos2[0] ,drawPos2[1] = getLineBoundaryPos(line) 

    if line.slope == None:
        line.slope = 0
    elif line.slope == 0:
        line.slope = None
    else:
        line.slope = -1.0/line.slope
    drawPos3[0] ,drawPos3[1] ,drawPos4[0] ,drawPos4[1] = getLineBoundaryPos(line)

if __name__ == '__main__':
    pyglet.app.run()