#TOPOLOGICAL SORT
#You're given a list of arbitrary jobs that need to be completed; these jobs are represented by distinct integers.
#You're also given a list of dependencies. A dependency is represented as a pair of jobs where the first job is a prerequisite of
#the second one. In other words, the second job depends on the first one; it can only be completed once the first job is completed.
#Write a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid order in which the given jobs can be completed. If no such order exists, the function should return an empty array.
import collections
class Graph:
    def __init__(self,graph,res,visited):
        self.graph=graph
        self.res=res
        self.visited=visited


def topologicalSort(jobs,deps):
    graph=collections.defaultdict(list)
    res=[]
    visited=[0]*(len(jobs)+1)
    Jobs=Graph(graph,res,visited)
    for pair in deps:
        Jobs.graph[pair[1]].append(pair[0])
    for i in jobs:
        if DFS(i,Jobs)==False:
            return []
    return Jobs.res
def DFS(node,Jobs):
    if Jobs.visited[node]==-1:
        return False
    if Jobs.visited[node]==1:
        return True
    Jobs.visited[node]=-1
    for i in Jobs.graph[node]:
        if DFS(i,Jobs)==False:
            return False

    Jobs.visited[node]=1
    Jobs.res.append(node)
    return True
if __name__=='__main__':

    jobs=[1,2,3,4]
    deps=[[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    print(topologicalSort(jobs,deps))
