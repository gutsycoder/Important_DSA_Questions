# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.
# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:
#
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:
#
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
import collections
import heapq
class Solution:
    def networkDelayTime(times, n: int, k: int) -> int:
        graph=collections.defaultdict(dict)

        for frm,to,cost in times:
            graph[frm][to]=cost

        distances={i: float('inf') for i in range(1,n+1)}
        distances[k]=0
        min_dist=[(0,k)]
        visited=set()

        while min_dist:
            cur_dist,cur=heapq.heappop(min_dist)
            if cur in visited:
                continue
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor in visited:
                    continue
                this_dist=cur_dist+graph[cur][neighbor]
                if this_dist<distances[neighbor]:
                    distances[neighbor]=this_dist
                    heapq.heappush(min_dist,(this_dist,neighbor))
        if len(visited)!=len(distances):
            return -1
        return distances[max(distances,key=distances.get)]



if __name__=="__main__":
    Edges=[[2,1,1],[2,3,1],[3,4,1]]
    n=4
    k=2
    print(Solution.networkDelayTime(Edges,n,k))
