#Dijkstras Algorithm
# You're given an integer start and a list edges of pairs of integers.
# The list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to the length of edges, where each indexi in edges contains vertex i 's outbound edges, in no particular order. Each individual edge is represented by an pair of two numbers, [destination, distance], where the destination is a positive integer denoting the destination vertex and the distance is a positive integer representing the length of the edge (the distance from vertex i to vertex destination ). Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination-not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).
# Write a function that computes the lengths of the shortest paths between start and all of the other vertices in the graph using Dijkstra's algorithm and returns them in an array. Each index i in the output array should represent the length of the
#shortest path between start and vertex i.If no path found from start to vertex i ,then output[i] should be -1
#Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to themselves) and will only have positively weighted edges (i.e., no negative distances).

#Time complexity O(v^2+e)
#Space complexity O(v)

def dijkstrasAlgorithm(start,edges):
    numberOfvertex=len(edges)
    minDistances=[float('inf') for i in range(numberOfvertex)]
    minDistances[start]=0
    visited=set()
    while len(visited)!=numberOfvertex:
        vertex,distance=getMinVertex(minDistances,visited)
        if distance==float('inf'):
            break
        visited.add(vertex)
        for edge in edges[vertex]:
            currentMinDistance=distance+edge[1]
            minDistances[edge[0]]=min(minDistances[edge[0]],currentMinDistance)
    return minDistances


def getMinVertex(minDistances,visited):
    vertex=None
    distance=float('inf')
    for i in range(len(minDistances)):
        if i not in visited:
            if minDistances[i]<=distance:
                distance=minDistances[i]
                vertex=i
    return vertex,distance







if __name__=='__main__':

    start=0
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    print(dijkstrasAlgorithm(start,edges))
