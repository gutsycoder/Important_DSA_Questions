# Given an undirected weighted connected graph, find the Really Special SubTree in it.
# The Really Special SubTree is defined as a subgraph consisting of all the nodes in the graph and:
# 1.There is only one exclusive path from a node to every other node.
# 2.The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
# 3.No cycles are formed
# To create the Really Special SubTree, always pick the edge with smallest weight.
# Determine if including it will create a cycle. If so, ignore the edge. If there are edges of equal weight available:
# 1.Choose the edge that minimizes the sum u+v+wt where u and v are vertices and wt is the edge weight.
# 2.If there is still a collision, choose any of them.
# 3.Print the overall weight of the tree formed using the rules.
# For example, given the following edges:
# u	v	wt
# 1	2	2
# 2	3	3
# 3	1	5
# First choose 1->2  at weight 2 . Next choose 2->3  at weight 3. All nodes are connected without cycles for a total weight of 3+2=5.


def root(vertex):
    global rootIDs
    if rootIDs[vertex]==vertex:
        return vertex
    else:
        while(rootIDs[vertex]!=vertex):
            rootIDs[vertex]=rootIDs[rootIDs[vertex]]
            vertex=rootIDs[vertex]
        return vertex
def union(x,y):

    Xroot=root(x)
    Yroot=root(y)
    rootIDs[Yroot]=Xroot

    return



def Kruskal(GE):
    global rootIDs
    minimumWeight=0
    for edge in GE:
        x,y,weight=edge[0],edge[1],edge[2]
        if root(x)!=root(y):
            minimumWeight+=weight
            union(x,y)
    return minimumWeight



if __name__=="__main__":
    V,E=4,6
    GE=[[1,2,5],[1,3,3],[4,1,6],[2,4,7],[3,2,4],[3,4,5]]
    GE=sorted(GE,key=lambda x:x[2])
    rootIDs=list(range(V+1))
    print(Kruskal(GE))
