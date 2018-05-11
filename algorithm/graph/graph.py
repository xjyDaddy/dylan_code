#Date:2018/5/8
#Author:dylan_xi
#Desc: graph class

class Graph(dict):
    def __init__(self , vs = [] , es = []):
        ''' create a new graph , (vs) is a list of verices ;
            (es) is a list of edges. '''
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)
        self.add_all_edges()
    def add_vertex(self , v):
        self[v] = {}
    def add_edge(self , e):
        v = e.getFrom()
        w = e.getTo()
        self[v][w] = e
    def get_edge(self, v ,w):
        if v in self:
            if w in self[v]:
                return self[v][w]
        return None
    def remove_edge(self ,v,w):
        e = self.get_edge(v ,w)
        if e:
            del self[v][w]
    def vertexs(self):
        return self.keys()
    def edges(self):
        edges = []
        for k , v in self.items():
            for eKey in v:
                edges.append(eKey)
        return edges
    def out_vertexs(self , v):
        vertexs = []
        if v in self:
            for w in self[v]:
                vertexs.append(w)
        return vertexs     
    def out_edges(self , v):
        edges = []
        if v in self:
            for _ ,e in self[v].items():
                edges.append(e)
        return edges
    def add_all_edges(self):
        '''make a edgeless graph to a complete graph'''
        for v1 in self:
            for v2 in self:
                if v1 is v2:
                    self.add_edge(Edge(v1 , v1 , 0))
                elif v2 not in self[v1]:
                    self.add_edge(Edge(v1 ,v2 , 999999))
    def formatPrint(self):
        for k , v in self.items():
            t = sorted(v.items())
            print(k ,t)
class Vertex(object):
    def __init__(self , lable):
        self.label = lable
    def __repr__(self):
        return '%s' % repr(self.label)
    __str__ = __repr__
    def __lt__(self ,other):
        return self.label < other.label

class Edge(object):
    def __init__(self , e1 , e2 , weight = 999999):
        self._vt = (e1 , e2)
        self._weight = weight
    def __repr__(self):
        return '%s-%s:%d'% (repr(self._vt[0]) , repr(self._vt[1]) , self._weight)
    def getFrom(self):
        return self._vt[0]
    def getTo(self):
        return self._vt[1]
    def getWeight(self):
        return self._weight
    def setWeight(self ,weight):
        self._weight = weight

'''
v = Vertex('v')
w = Vertex('w')
e = Edge(v ,w)
print(e)
graph  = Graph([v,w] , [e])
print(graph)
print(graph.get_edge(Vertex('z') ,v))
print(graph.get_edge(v ,w))
print(graph.edges())
print(graph.vertexs())
print(graph.out_vertexs(v))
print(graph.out_edges(v))
print(graph.remove_edge(v ,w))
print(graph)
print('-----------------------add_all_edges-----------------')
graph.add_vertex(Vertex('q'))
graph.add_all_edges()
print(graph)

'''