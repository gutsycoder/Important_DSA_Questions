#Implement Tarjan's Algorithm #This graph is a Directed Graph. Edges are given in the form of [u,v] u-->v

discoveryTime=1
def dfs(graph,node,disc,low,inStack,nodeStack,ans):
    global discoveryTime
    disc[node]=discoveryTime
    low[node]=discoveryTime
    discoveryTime+=1
    nodeStack.append(node)
    inStack[node]=True
    #Using Tarjan's Algorithm
    for v in graph[node]:
        #Looking  all unvisited node
        if disc[v]==-1:
            dfs(graph,v,disc,low,inStack,nodeStack,ans)
            low[node]=min(low[node],low[v])
        elif inStack[v]:
            low[node]=min(low[node],low[v]) #Here we could also use low[node]=min(low[node],dis[v])
    if low[node]==disc[node]:
        component=[]
        #u is the topmost element in the stack
        u=0
        while nodeStack[-1]!=node:
            u=nodeStack.pop()
            inStack[u]=False
            component.append(u)
        u=nodeStack.pop()
        inStack[u]=False
        component.append(u)
        ans.append(component)


def stronglyConnectedComponent(n,edges):
    graph=[[] for i in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    disc=[-1]*n
    low=[-1]*n
    nodeStack=[]
    inStack=[False]*n
    ans=[]

    for i in range(n):
        if disc[i]==-1:
            dfs(graph,i,disc,low,inStack,nodeStack,ans)

    return ans



















if __name__=="__main__":
    vertex=5
    edges=[[0,1],[1,2],[1,4],[2,3],[3,2],[4,0]]
    print(stronglyConnectedComponent(vertex,edges))
