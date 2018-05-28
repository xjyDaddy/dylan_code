#Date:2018/5/28
#Author:dylanxi
#Desc:Rect class

class Rect2:
    def __init__(self,x ,y,width ,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def isContainPoint(self,point):
        return point.x < self.x + self.width  and point.x > self.x and\
               point.y < self.y + self.height and point.y > self.y 