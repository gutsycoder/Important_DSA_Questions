#Find the number of unique cycle in the Undirected Graph

#The problem with this code is that i doesn't contains unique cycles. It gives twice the unique cycles maybe
component=[]
def find_Cycle(graph):
    n=len(graph)
    visited=[False]*n
    for i in range(n):
        component=[]
        dfs(graph,visited,i,i,None)
        visited=[False]*n
        for j in range(i+1):
            visited[j]=True
def dfs(graph,visited,node,origin,parent):
    global cycle
    global component
    if node==origin and visited[node]:
        component.append(node)
        print(component)
        component.pop()
        cycle+=1
        print("Cycle++")
        return
    if visited[node]:
        return
    visited[node]=True
    neighbor=graph[node]
    component.append(node)
    for index,value in enumerate(neighbor):
        if index!=parent and value==1:
            #print(node,index)
            dfs(graph,visited,index,origin,node)
        if parent==None:
            visited[index]=True

    component.pop()
    # for index,value in enumerate(neighbor):
    #     visited[index]=False


    visited[node]=False






if __name__=="__main__":
    #graph=[[0,1,1,1,0],[1,0,1,0,1],[1,1,0,1,1],[1,0,1,0,0],[0,1,1,0,0]]
    #graph=[[0,1,0,0,1],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,1],[1,0,0,1,0]]
    #graph=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
    graph=[[0,1,0,0,0],[1,0,1,1,0],[0,1,0,0,1],[0,1,0,0,1],[0,0,1,1,0]]
    cycle=0
    find_Cycle(graph)
    print(cycle)
