Given an undirected weighted connected graph, find the Really Special SubTree in it.
The Really Special SubTree is defined as a subgraph consisting of all the nodes in the graph and:
1.There is only one exclusive path from a node to every other node.
2.The subgraph is of minimum overall weight (sum of all edges) among all such subgraphs.
3.No cycles are formed
To create the Really Special SubTree, always pick the edge with smallest weight.
Determine if including it will create a cycle. If so, ignore the edge. If there are edges of equal weight available:
1.Choose the edge that minimizes the sum u+v+wt where u and v are vertices and wt is the edge weight.
2.If there is still a collision, choose any of them.
3.Print the overall weight of the tree formed using the rules.
For example, given the following edges:
u	v	wt
1	2	2
2	3	3
3	1	5
First choose 1->2  at weight 2 . Next choose 2->3  at weight 3. All nodes are connected without cycles for a total weight of 3+2=5 .
