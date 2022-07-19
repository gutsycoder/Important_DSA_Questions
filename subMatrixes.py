def printMatrix(matrix,rStart,rSize,cStart,cSize):
     for i in range(rStart,rStart+rSize):
          for j in range(cStart,cStart+cSize):
               print(matrix[i][j],end="" )
          print()
     print("***********************************")




matrix=[[0,1,0],[1,2,3],[1,1,1]]
res=0
m=len(matrix)
n=len(matrix[0])
for rowStart in range(m):
     rowSize=1
     while rowStart+rowSize<=m:
          for colStart in range(n):
               colSize=1
               while colStart+colSize<=n:
                    printMatrix(matrix,rowStart,rowSize,colStart,colSize)
                    colSize+=1
          rowSize+=1
