#Date:2018/5/26
#Author:dylan_xi
#Desc:PariticleSystem 
from Vec2 import Vec2
from pariticle import Pariticle
from Color4b import Color4b
from Segment import Segment
from Rect2 import Rect2
from quarterTree import QuarterTree
import mathUtils
import math
import random
import Config
class PariticleSystem():
    param = {
        #Where praticle spawn from
        'pos' : Vec2(Config.screenSize[0]/2 ,Config.screenSize[1]/2) , 
        #How many pariticles spawn every second
        'praticlePerSecond': 5,
        #How long each pariticle lives(and how much this can vary)
        'pariticleLife': 2,
        'lifeVariation': 0.52,
        #The gradient of colors the particle will travel through
        'colorFrom': Color4b(255, 0, 255, 255),
        'colorTo': Color4b(0, 255, 255, 100),
        #The angle the particle will fire off at (and how much this can vary)
        'angle': 0,
        'angleVariation': math.pi * 2,
 
        #The velocity range the particle will fire off at
        'minVelocity' : 50,
        'maxVelocity' : 100,
 
        #The gravity vector applied to each particle
        'gravity': Vec2(0, 30.8),
 
        #An object to test for collisions against, and bounce damping factor
        #for said collisions
        'colliders' : [],  
        'bounceDamper': 0.5
    }

    def __init__(self, param = None):
        if param:
            for k , v in self.param.items():
                self.param[k] = param[k]
        self.pariticles = []
        self.quterTree = QuarterTree(Rect2(0 , 0 , Config.screenSize[0] , Config.screenSize[1]),1)
        self.randomColliders()
        self.quterTree.insert(self.param['colliders'])
    def update(self , dt):
        self.step(dt)
        self.updateSpawn(dt)
    def step(self ,dt):
        deadList = []
        for pariticle in self.pariticles:
            pariticle.step(dt)
            if pariticle.isDead():
                deadList.append(pariticle)
        for deadPariticle in deadList:
            self.pariticles.remove(deadPariticle)
    def updateSpawn(self , dt):
        frameNum = math.ceil(dt *self.param['praticlePerSecond'])
        for i in range(frameNum):
            self.spawnPariticle((1.0+i) / frameNum * dt)
    def spawnPariticle(self , offset):
        angle = mathUtils.ramdomRange(self.param['angle'] , self.param['angle'] + self.param['angleVariation'])
        speed = mathUtils.ramdomRange(self.param['minVelocity'] , self.param['maxVelocity'])
        lifetime = mathUtils.ramdomRange(self.param['pariticleLife'] , self.param['pariticleLife'] + self.param['lifeVariation'])
        velocity = mathUtils.fromPolar(angle , speed)
        pos = self.param['pos'] + velocity* offset 
        self.pariticles.append(Pariticle(self , pos , velocity, lifetime))

    def draw(self , render):
        for pariticle in self.pariticles:
            pariticle.draw(render)
        if self.param['colliders']:
            for collider in self.param['colliders']:
                collider.draw(render)
        if(self.quterTree):
            self.quterTree.draw(render)

    def randomVec(self):
        return Vec2(random.random()*Config.screenSize[0] ,random.random()*Config.screenSize[1])
    def randomColliders(self):
        for i in range(100):
            self.param['colliders'].append(Segment(self.randomVec() , self.randomVec()))