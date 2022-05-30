#Find Bridges In the Graph
"""
    Time Complexity : O(V + E)
    Space Complexoty : O(V)

    Where V is the number of vertices and E is the number of edges in the graph.
"""

time = 0


def dfs(graph, allBridges, visited, ins, low, parent, currentVertex):

    # Mark currentVertex as visited.
    visited[currentVertex] = True

    # Initialize discovery time and low value
    global time
    time += 1
    low[currentVertex] = ins[currentVertex] = time

    # Iterate all the adjacent vertices to currentVertex node.
    for child in graph[currentVertex]:
        # child is the current adjacent vertex of currentVertex

        # If child is not visited yet then recur for it.
        if not visited[child]:

            dfs(graph, allBridges, visited, ins, low, currentVertex, child)

            # Check if the subtree rooted with child has a connection to one of the
            # ancestors of currentVertex
            low[currentVertex] = min(low[child], low[currentVertex])

            if low[child] > ins[currentVertex]:
                # Add an edge(currentVertex-child) to answer.
                allBridges.append([currentVertex,child])

        elif child != parent:
            # If adjacent vertex is alreedy visited before, then update the low of currentVertex.
            low[currentVertex] = min(low[currentVertex], ins[child]) #can also write min(low[currentVertex],low[child])


# Function to add edge to graph.
def addedge(graph, a, b):
    graph[a].append(b)
    graph[b].append(a)


def findBridges(edges, v, e):
    graph = [[] for i in range(v)]

    # Adding edges in the graph.
    for ei in range(e):

        a = edges[ei][0]
        b = edges[ei][1]

        addedge(graph, a, b)

    # Initialise time to 0
    global time
    time = 0

    # It keep track of visited vertices.
    visited = [0] * v

    # It stores discovery time of every vertex
    ins = [0] * v

    # For every vertex it stores, the discovery time of the earliest discovered
    # vertex to which or any of the vertices in the subtree rooted at is
    # having a back edge.
    low = [0] * v

    allBridges = []

    # Call the recursive helper function to find bridges in DFS tree rooted with
    # vertex i.
    for i in range(v):
        if not visited[i]:
            dfs(graph, allBridges, visited, ins, low, -1, i)

    return allBridges
if __name__=="__main__":
    edges=[[0,1],[3,1],[1,2],[3,4]]
    vertex=5
    edge=4
    print(findBridges(edges,vertex,edge))
