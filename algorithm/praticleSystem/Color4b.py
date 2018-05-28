#Date:2018/5/26
#Author:dylan_xi
#Desc:Point class

class Color4b:
    def __init__(self,r ,g , b , a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    def __add__(self , other):
        return Color4b(self.r + other.r , self.g + other.g , self.b + other.b , self.a + other.a)
    def __sub__(self, other):
        return Color4b(self.r - other.r , self.g - other.g , self.b - other.b , self.a - other.a)
    def __repr__(self):
        return "Color4b(r = {0} , g = {1} , b = {2} , a = {3})" .format(self.r , self.g , self.b ,self.a)
    def __mul__(self, factor):
        return Color4b(self.r *factor , self.g *factor , self.b *factor , self.a *factor)
    def lerp(self , dstColor , percent):
        return self+(dstColor - self)*percent