#Date:2018/5/26
#Author:dylan_xi
#Desc:mathUtils
import math
import random
from Vec2 import Vec2
from Rect2 import Rect2
import Config
def fromPolar(angle , speed):
    return Vec2(speed * math.sin(angle) , speed * math.cos(angle))

def ramdomRange(varFrom , varTo):
    ratio = random.random()
    return varFrom + (varTo - varFrom) * ratio

def vecCrossProduct(vec1 , vec2):
    return vec1.x * vec2.y - vec2.x * vec1.y

def vecDotProduct(vec1 , vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y

def rectIntersection(a , b , c , d):
    return  max(a.x , b.x) >= min(c.x ,d.x)\
            and min(a.x , b.x) <= max(c.x ,d.x)\
            and max(a.y , b.y) >= min(c.y ,d.y)\
            and min(a.y , b.y) <= max(c.y ,d.y)
# a-b 是否跨立 c-d ,如果跨立成功那么 a-b 在 c-d 所在直线两侧
def isStraddle(a , b , c , d):
    return vecCrossProduct(a-c , d-c) * vecCrossProduct(b-c , d-c) <= 0

def segmentIntersection(a , b , c , d):
    Config.collisionDetectTimes += 1
    #先做排除实验
    if not rectIntersection(a,b , c ,d):
        return False
    #再做跨立实验
    if isStraddle(a,b,c,d) and isStraddle(c,d,a,b):
        return True
    else:
        return False

def reflect(segment , vec):
    normalVec = segment.getUnitNormalVec()
    result = vec - normalVec*vecDotProduct(normalVec , vec)*2
    return result
def getLenght(vec):
    return math.sqrt(vec.x * vec.x + vec.y * vec.y)    

def rectSegmentIntersection(rect , seg):
    #先检测线段是否在矩形内部
    if rect.isContainPoint(seg.p1) or rect.isContainPoint(seg.p2):
        return True
    #再检测是否和四个边交叉
    if segmentIntersection(Vec2(rect.x , rect.y) , Vec2(rect.x , rect.y + rect.height), seg.p1 , seg.p2):
        return True
    if segmentIntersection(Vec2(rect.x+rect.width , rect.y) , Vec2(rect.x+rect.width , rect.y + rect.height), seg.p1 , seg.p2):
        return True        
    if segmentIntersection(Vec2(rect.x , rect.y) , Vec2(rect.x+rect.width , rect.y), seg.p1 , seg.p2):
        return True
    if segmentIntersection(Vec2(rect.x , rect.y+rect.height) , Vec2(rect.x+rect.width , rect.y + rect.height), seg.p1 , seg.p2):
        return True
    return False
if __name__ == "__main__" :
    a = Vec2(1, 1)
    b = Vec2 (2 ,2)
    c = Vec2 (3,4)
    d = Vec2 (2,3)
    print(segmentIntersection(a,b,c,d))
