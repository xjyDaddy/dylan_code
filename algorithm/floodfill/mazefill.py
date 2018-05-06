#Date:2018/5/6
#Author:dylan_xi
#Desc:use dfs to fill maze , the algorithm' name: floodfill
import copy 
class FloodFill:
    def __init__(self , mazeDatas):
        self._mazeDatas = copy.deepcopy(mazeDatas)
        self._result = None
        self._mazeWidth = len(self._mazeDatas[0])
        self._mazeHeight = len(self._mazeDatas)
        self._clearBook()
        self._next = [[1,0] , [0,-1] , [-1,0] , [0,1]]        
    def _clearBook(self):
        self._book = []        
        for x in range(0, self._mazeHeight):
            self._book.append([0]*self._mazeWidth)
    def fillWithTarget(self,x , y , color):
        self._clearBook()
        self._resultMaze = copy.deepcopy(self._mazeDatas)
        self._dfs(x, y ,color)
        self._clearBook()
        return self._resultMaze
    def _dfs(self,x , y , color):
        self._book[y][x] = 1
        self._resultMaze[y][x] = color        
        for next in self._next:
            nextX = next[0] + x
            nextY = next[1] + y
            if self._mazeWidth > nextX and self._mazeHeight > nextY and nextX >=0 and nextY >=0:
                if self._book[nextY][nextX] == 0 and self._resultMaze[nextY][nextX] > 0:
                    self._book[nextY][nextX] = 1
                    self._resultMaze[nextY][nextX] = color
                    self._dfs(nextX , nextY ,color)
    def getIndependentAreaNum(self):
        num = 0
        self._resultMaze = copy.deepcopy(self._mazeDatas)
        for y in range(0 , self._mazeHeight):
            for x in range(0 , self._mazeWidth):
                if(self._resultMaze[y][x] > 0):
                    num = num + 1
                    self._dfs(x , y, -num)
        return num , self._resultMaze
# test
mazeDatas = [
    [1,2,1,0,0,0,0,0,2,3],
    [3,0,2,0,1,2,1,0,1,2],
    [4,0,1,0,1,2,3,2,0,1],
    [3,2,0,0,0,1,2,4,0,0],
    [0,0,0,0,0,0,1,5,3,0],
    [0,1,2,1,0,1,5,4,3,0],
    [0,1,2,3,1,3,6,2,1,0],
    [0,0,3,4,8,9,7,5,0,0],
    [0,0,0,3,7,8,6,0,1,2],
    [0,0,0,0,0,0,0,0,1,0],
]

f = FloodFill(mazeDatas)

result =f.fillWithTarget(6,8,-1)
for t in result:
    print(t)

num , result2 = f.getIndependentAreaNum()
print(num)
for t in result2:
    print(t)
