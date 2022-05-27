#Bellman-Ford Algorithm
# Given a graph and a source vertex src in graph,
# find shortest paths from src to all vertices in the given graph. The graph may contain negative weight edges.
#Time complexity of Bellman-Ford is O(VE)
class Graph:

    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def printArr(self,dist):
        print("Vertex   Distance from Source ")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i,dist[i]))

    def BellmanFord(self,src):
        dist=[float('inf')]*self.V
        dist[src]=0

        for i in range(self.V-1):

            for u,v,w in self.graph:
                if dist[u]!=float('inf') and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
        for u,v,w in self.graph:
            if dist[u]!=float('inf') and dist[u]+w<dist[v]:
                print("Graph contains the Negative Cycle")
                return
        self.printArr(dist)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
g.BellmanFord(0)
