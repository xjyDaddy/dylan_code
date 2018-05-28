#Date:2018/5/28
#Author:dylan_xi
#Desc:quarterTree
from Rect2 import Rect2
from Vec2 import Vec2
import mathUtils
import wx
class QuarterTree(object):
    SPLITE_MAX_NUM = 3
    MAX_DEEPTH = 5
    def __init__(self, rect , deepth):
        self._trees = []
        self._rect = Rect2(rect.x , rect.y , rect.width , rect.height)
        self._deepth = deepth
        self._isSplite = False
        self._segs = []
    def splite(self): 
        self._isSplite = True
        w2 = self._rect.width/2
        h2 = self._rect.height/2
        x = self._rect.x
        y = self._rect.y
        deepth = self._deepth + 1
        self._trees.append(QuarterTree(Rect2(x , y ,w2 , h2),deepth))
        self._trees.append(QuarterTree(Rect2(x+w2 , y ,w2 , h2),deepth))
        self._trees.append(QuarterTree(Rect2(x , y+h2 ,w2 , h2),deepth))
        self._trees.append(QuarterTree(Rect2(x+w2 , y+h2 ,w2 , h2),deepth))

        for tree in self._trees:
            tree.insert(self._segs)
        self._segs = []
    def insert(self , segments):
        for segment in segments:
            if mathUtils.rectSegmentIntersection(self._rect , segment):
                self._segs.append(segment)
        if len(self._segs) >= QuarterTree.SPLITE_MAX_NUM and  self._deepth <= QuarterTree.MAX_DEEPTH:
            if not self._isSplite:
                self.splite()

    def overlapsWithLine(self , segment):
        return mathUtils.rectIntersection(Vec2(self._rect.x , self._rect.y) ,Vec2(self._rect.x + self._rect.width, self._rect.y+ self._rect.height) , segment.p1 , segment.p2)
    def getInterSection(self , segment):
        if not self.overlapsWithLine(segment):
            return None
        for seg in self._segs:
            if mathUtils.segmentIntersection(seg.p1 , seg.p2 , segment.p1 , segment.p2):
                return seg
        for tree in self._trees:
            targetSeg = tree.getInterSection(segment)
            if(targetSeg):
                return targetSeg
        return None

    def draw(self, render):
        pen = wx.Pen()
        pen.SetStyle(wx.PENSTYLE_SOLID)
        pen.SetColour( wx.Colour(255 -self._deepth*50, 255-self._deepth*50,0))
        pen.SetWidth(3)
        render.SetPen(pen)
        x = self._rect.x
        y = self._rect.y
        w2 = self._rect.width/2
        h2 = self._rect.height/2
        w = 2*w2
        h = 2*h2
        if self._isSplite:
            render.DrawLine(x, y +h2 , x+w , y+h2)
            render.DrawLine(x+w2, y , x+w2 , y+h)
        if len(self._segs) != 0:
            render.DrawText(str(len(self._segs)) , x+w2 , y +h2)
        for tree in self._trees:
            tree.draw(render)