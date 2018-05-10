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
    def add_vertex(self , v):
        self[v] = {}
    def add_edge(self , e):
        ''' add edge to the graph by adding an entry in both directions
        If there is already an edge connecting these Vertices , the new edge replaces
        it ''' 
        v , w  = e
        self[v][w] = e
        self[w][v] = e
    def get_edge(self, v ,w):
        if v in self:
            if w in self[v]:
                return self[v][w]
        return None
    def remove_edge(self ,v,w):
        e = self.get_edge(v ,w)
        if e:
            del self[v][w]
            del self[w][v]
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
                edges.append(w)
        return edges
    def add_all_edges(self):
        '''make a edgeless graph to a complete graph'''
        for v1 in self:
            print(v1)
            for v2 in self:
                print(v1 ,v2)
                if (v1 is not v2) and (v2 not in self[v1]):
                    self.add_edge(Edge(v1 ,v2))
    

class Vertex(object):
    def __init__(self , lable):
        self.label = lable
    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)
    __str__ = __repr__

class Edge(tuple):
    def __new__(cls , e1 , e2):
        return tuple.__new__(cls , (e1 ,e2))
    def __repr__(self):
        return 'Edge(%s , %s)'% (repr(self[0]) , repr(self[1]))
    
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