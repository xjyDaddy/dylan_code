#Date:2018/5/8
#Author:dylan_xi
#Desc: floyd_warshall algorithm: get each pair of vertexs 's shortest path, 
# Multi-source shortest path.

import sys
sys.path.append('../graph')
from graph import Graph , Edge , Vertex


va = Vertex('A')
vb = Vertex('B')
vc = Vertex('C')
vd = Vertex('D')

e1 = Edge(va , vb , 2)
e2 = Edge(va , vc , 6)
e3 = Edge(va , vd , 4)
e4 = Edge(vb , vc , 3)
e5 = Edge(vc , va , 7)
e6 = Edge(vc , vd , 1)
e7 = Edge(vd , va , 5)
e8 = Edge(vd , vc , 12)

g = Graph([va , vb , vc , vd] , [e1 ,e2, e3,e4,e5,e6,e7,e8])

for k in g.vertexs():
    for j in g.vertexs():
        for i in g.vertexs():   
            e1 = g.get_edge(i , k)
            e2 = g.get_edge(k , j)
            e3 = g.get_edge(i , j)
            if e1.getWeight() + e2.getWeight() < e3.getWeight():
                e3.setWeight(e1.getWeight() + e2.getWeight())

g.formatPrint()