#Date:2018/5/8
#Author:dylan_xi
#Desc: dijkstra algorithm: get one vertex to other vertexs' shortest path
import sys
sys.path.append('../graph')
from graph import Graph , Edge , Vertex

v1 = Vertex('1')
v2 = Vertex('2')
v3 = Vertex('3')
v4 = Vertex('4')
v5 = Vertex('5')
v6 = Vertex('6')

e1 = Edge(v1 , v2 , 1)
e2 = Edge(v1 , v3 , 12)
e3 = Edge(v2 , v3 , 9)
e4 = Edge(v2 , v4 , 3)
e5 = Edge(v4 , v3 , 4)
e6 = Edge(v4 , v5 , 13)
e7 = Edge(v3 , v5 , 5)
e8 = Edge(v5 , v6 , 4)
e9 = Edge(v4 , v6 , 15)

g = Graph([v1,v2,v3,v4,v5,v6] , [e1 ,e2,e3,e4,e5,e6,e7,e8])

class Dijkstra:
    _INF_DIS = 9999999
    def __init__(self , graph):
        self._g = graph
        self._dis = {}
        self._parent = {}
        self._result = {}
        self._book = {} 
        self._fromVertex = None
    def _isRelaxationOver(self):
        for flag in self._book.values():
            if flag == 0:
                return False
        return True
    def _getVertexByShortestDis(self):
        shortestDis = Dijkstra._INF_DIS
        shortestVertex = None
        for vertex in self._getNotRelaxationVertexs():
            if shortestDis > self._dis[vertex]:
                shortestDis = self._dis[vertex]
                shortestVertex = vertex
        return shortestVertex
    def _initFromSearch(self , fromVertex):
        for toVertex in self._g.vertexs():
            edge = self._g.get_edge(fromVertex , toVertex) 
            self._book[toVertex] = 0
            self._parent[toVertex] = fromVertex
            if edge:
                self._dis[toVertex] = edge.getWeight()
            else:
                if toVertex is fromVertex :
                    self._dis[toVertex] = 0
                    self._book[toVertex] = 1                    
                else:
                    self._dis[toVertex] = Dijkstra._INF_DIS
    def _getNotRelaxationVertexs(self):
        for k , v in self._book.items():
            if v == 0:
                yield k
    def _relaxation(self , vertex):
        for notRelaxationVertex in self._getNotRelaxationVertexs():
            if notRelaxationVertex is vertex:
                continue
            dis1  = self._dis[vertex]
            dis2 = Dijkstra._INF_DIS
            if self._g.get_edge(vertex , notRelaxationVertex):
                dis2 = self._g.get_edge(vertex , notRelaxationVertex).getWeight()
            dis3 = self._dis[notRelaxationVertex]
            if dis3 > dis1 + dis2:
                self._dis[notRelaxationVertex] = dis1 + dis2
                self._parent[notRelaxationVertex] = vertex
    def getShortestPaths(self , fromVertex):
        self._initFromSearch(fromVertex)
        while not self._isRelaxationOver():
            shortestDisVertex = self._getVertexByShortestDis()
            if not shortestDisVertex:
                break    
            self._book[shortestDisVertex] = 1
            self._relaxation(shortestDisVertex)
        return self._dis , self._parent

#test
dijkstra = Dijkstra(g)
result1 , result2 = dijkstra.getShortestPaths(v1)
print(result1)
print(result2)