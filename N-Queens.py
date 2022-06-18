#Non-Attacking Queens
# Write a function that takes in a positive integer n and returns the number of non-attacking placements
# of n queens on an n x n chessboard.
# A non-attacking placement is one where no queen can attack another queen in a single turn. In other words,
#it's a placement where no queen can move to the same position as another queen in a single turn.
# In chess, queens can move any number of squares horizontally, vertically, or diagonally in a single turn.
# The chessboard above is an example of a non-attacking placement of 4 queens on a 4x4 chessboard.
# For reference, there are only 2 non-attacking placements of 4 queens on a 4x4 chessboard.
#Sample Input n=4
#Sample Output 2

def nonAttackingQueens(n):
    columnPlacements=[0]*n
    return getNumberOfNonAttackingQueenPlacements(0,columnPlacements,n)

def getNumberOfNonAttackingQueenPlacements(row,columnPlacements,boardSize):
    if row==boardSize:
        return 1
    validPlacements=0
    for col in range(boardSize):
        if isNonAttackingPlacement(row,col,columnPlacements):
            columnPlacements[row]=col
            validPlacements+=getNumberOfNonAttackingQueenPlacements(row+1,columnPlacements,boardSize)

    return validPlacements
#as Row tends to n , this becomes a O(n) Algorithm
def isNonAttackingPlacement(row,col,columnPlacements):
    for previousRow in range(row):
        columnToCheck=columnPlacements[previousRow]
        sameColumn=columnToCheck==col
        onDiagonal=abs(col-columnToCheck)==row-previousRow
        if onDiagonal or sameColumn:
            return False

    return True





if __name__=="__main__":
    n=4
    print(nonAttackingQueens(n))
