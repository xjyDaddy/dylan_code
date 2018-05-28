#Date:2018/5/26
#Author:dylanxi
#Desc:Segment class
from Vec2 import Vec2
import math
import wx
class Segment:
    def __init__(self,p1 ,p2):
        self.p1 = Vec2(p1.x , p1.y)    
        self.p2 = Vec2(p2.x , p2.y)
    
    def getUnitNormalVec(self):
        vec = self.p2 - self.p1
        lenght = math.sqrt(vec.x * vec.x + vec.y * vec.y)
        normalVec = Vec2(-vec.y/lenght , vec.x/lenght)
        return normalVec

    def draw(self, render):
        pen = wx.Pen()
        pen.SetStyle(wx.PENSTYLE_SOLID)
        pen.SetColour( wx.Colour(0, 0,255))
        pen.SetWidth(5)
        render.SetPen(pen)
        render.DrawLine(self.p1.x, self.p1.y , self.p2.x , self.p2.y)
    def __repr__(self):
        return "Segment({0} , {1})" .format(self.p1 , self.p2)