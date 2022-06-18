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
    blockedColumns=set()
    blockedLeftDiagonals=set()
    blockedRightDiagonals=set()

    return getNumberOfNonAttackingQueenPlacements(0,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals,n)

def getNumberOfNonAttackingQueenPlacements(row,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals,boardSize):
    if row==boardSize:
        return 1

    validPlacements=0
    for col in range(boardSize):
        if isNonAttackingPlacements(row,col,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals):
            placeQueen(row,col,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals)
            validPlacements+=getNumberOfNonAttackingQueenPlacements(row+1,
                                                                   blockedColumns,blockedLeftDiagonals,blockedRightDiagonals,boardSize)
            removeQueen(row,col,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals)
    return validPlacements
#This is a O(1) method
def isNonAttackingPlacements(row,col,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals):
    if col in blockedColumns:
        return False
    if row+col in blockedLeftDiagonals:
        return False
    if row-col in blockedRightDiagonals:
        return False

    return True

def placeQueen(row,col,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals):
    blockedColumns.add(col)
    blockedLeftDiagonals.add(row+col)
    blockedRightDiagonals.add(row-col)

def removeQueen(row,col,blockedColumns,blockedLeftDiagonals,blockedRightDiagonals):
    blockedColumns.remove(col)
    blockedLeftDiagonals.remove(row+col)
    blockedRightDiagonals.remove(row-col)


if __name__=="__main__":
    n=4
    print(nonAttackingQueens(n))
