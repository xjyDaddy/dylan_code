#Date:2018/5/26
#Author:dylan_xi
#Desc:pariticle elem use in systems
from Vec2 import Vec2
from Segment import Segment
import mathUtils
import wx
import Config
class Pariticle():
    def __init__(self, pariticleSystem , pos , velocity, lifetime):
        self._params = pariticleSystem.param
        self._pariticleSystem = pariticleSystem 
        self._pos = pos
        self._velocity = velocity
        self._lifeTime = lifetime
        self._elapseTime = 0
    def step(self , dt):
        self._elapseTime += dt
        lastPos = Vec2(self._pos.x , self._pos.y)
        self._velocity += self._params['gravity'] * dt
        self._pos += self._velocity*dt
        isFast = True
        if isFast:
            if self._params['colliders']:
                segment = Segment(self._pos , lastPos)
                collider = self._pariticleSystem.quterTree.getInterSection(segment)
                if collider:
                    self._pos = lastPos
                    self._velocity = mathUtils.reflect(collider , self._velocity)*self._params['bounceDamper']                    
        else:
            if self._params['colliders']:
                segment = Segment(self._pos , lastPos)
                for collider in self._params['colliders']:
                    if mathUtils.segmentIntersection(segment.p1 , segment.p2 , collider.p1 , collider.p2):
                        self._pos = lastPos
                        self._velocity = mathUtils.reflect(collider , self._velocity)*self._params['bounceDamper']
                        break
    def isDead(self):
        return self._elapseTime >= self._lifeTime
    def draw(self , render):
        lifePercent = self._elapseTime / self._lifeTime
        color = self._params['colorFrom'].lerp(self._params['colorTo'] , lifePercent)
        render.SetBrush(wx.Brush(wx.Colour(int(color.r) , int(color.g) , int(color.b) , int(color.a)), wx.BRUSHSTYLE_SOLID)) 
        pen = wx.Pen()
        pen.SetStyle(wx.PENSTYLE_TRANSPARENT)
        render.SetPen(pen)
        render.DrawCircle(self._pos.x, self._pos.y, 2)
    