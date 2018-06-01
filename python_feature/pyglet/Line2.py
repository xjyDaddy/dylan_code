#Date:2018/5/26
#Author:dylanxi
#Desc:Line2 class

class Line2:
    def __init__(self, x1,y1,x2,y2):
        if (x2 - x1) == 0:
            self.slope = None
        else:
            self.slope = (y2-y1)/(x2-x1)
        self.x1 = x1
        self.y1 = y1
    def getSlope(self):
        return self.slope
    def setSlope(self , slope):
        self.slope = slope
    def getIntercept(self):
        if self.slope: 
            return self.y1 - self.slope*self.x1
    def getY(self,x):
        if self.slope == None:
            return None
        return self.slope*(x - self.x1) + self.y1 
    def getX(self , y):
        if self.slope == None:
            return self.x1
        if self.slope == 0:
            return None
        return (y-self.y1)/self.slope + self.x1
