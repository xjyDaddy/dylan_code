#Date:2018/5/26
#Author:dylanxi
#Desc:Vec2 class

class Vec2:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def __add__(self , other):
        return Vec2(self.x + other.x , self.y + other.y)
    def __sub__(self, other):
        return Vec2(self.x - other.x , self.y - other.y)
    def __repr__(self):
        return "Vec2({0} , {1})" .format(self.x , self.y)
    
    def __rmul__(self, factor):
        return Vec2(self.x * factor , self.y * factor)
    def __mul__(self, factor):
        return Vec2(self.x * factor , self.y * factor)
    def lerp(self , dstVec2 , percent):
        return self+(dstVec2 - self)*percent

if __name__ == "__main__" :
    p1 = Vec2(2, 3)
    p2 = Vec2 (4 ,6)
    print(p1.lerp(p2 , 0.5))
