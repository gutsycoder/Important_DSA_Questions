# River Sizes
# You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only @s and 1 s.
#Each represents land, and each 1 represents part of a river.
#A river consists of any number of 1 s that are either horizontally or vertically adjacent (but not diagonally adjacent).
#The number of adjacent 1 s forming a river determine its size.
# Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line;
#it can be L-shaped, for example.
# Write a function that returns an array of the sizes of all rivers represented in the input matrix.
# The sizes don't need to be in any particular order.
# matrix = [
# [1, 0, 0, 1, 0],
# [1, 0, 1, 0, 0],
# [0, 0, 1, 0, 1],
# [1, 0, 1, 0, 1],
# [1, 0, 1, 1, 0]
# ]
# output=[1,2,2,2,5]
def riverSizes(matrix):

  sizes=[]
  visited=[[False for value in row]for row in matrix]
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if visited[i][j] or matrix[i][j]==0:
        continue
      currentSize=traverseNodes(i,j,matrix,visited,sizes)
      if currentSize>0:
        sizes.append(currentSize)

  return sizes

def traverseNodes(i,j,matrix,visited,sizes):
  if visited[i][j] or matrix[i][j]==0:
    return 0
  unvisitedNeighbors=getUnvisitedNeighbors(i,j,matrix,visited)
  currentSize=1
  visited[i][j]=True
  for i,j in unvisitedNeighbors:
    currentSize+=traverseNodes(i,j,matrix,visited,sizes)
  return currentSize



def getUnvisitedNeighbors(i,j,matrix,visited):
  unvisitedNeighbors=[]
  if i>0 and not visited[i-1][j]:
    unvisitedNeighbors.append([i-1,j])
  if i<len(matrix)-1 and not visited[i+1][j]:
    unvisitedNeighbors.append([i+1,j])
  if j>0 and not visited[i][j-1]:
    unvisitedNeighbors.append([i,j-1])
  if j<len(matrix[0])-1 and not visited[i][j+1]:
    unvisitedNeighbors.append([i,j+1])
  return unvisitedNeighbors

if __name__=="__main__":


    matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
    ]
    print(riverSizes(matrix))
