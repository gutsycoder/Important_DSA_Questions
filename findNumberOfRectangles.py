#FIND TOTAL NUMBER OF RECTANGLES
# Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and
# returns the number of rectangles formed by these coordinates.
# A rectangle must have its four corners amongst the coordinates in order to be counted, and
# we only care about rectangles with sides parallel to the x and y axes (i.e., with horizontal and
# vertical sides--no diagonal sides).
# You can also assume that no coordinate will be farther than 100 units from the origin.
# Sample Input
# coords = [
# [0, 0], [0, 1], [1, 1], [1, 0],
# [2, 1], [2, 0], [3, 1], [3, 0]]
# Output = 6
def rectangleMania(coords):
    coordsTable=getCoordsTable(coords)
    return getRectangleCount(coords,coordsTable)

def getCoordsTable(coords):
    coordsTable={}
    for coord in coords:
        coordString=coordToString(coord)
        coordsTable[coordString]=True
    return coordsTable

def getRectangleCount(coords,coordsTable):
    rectangleCount=0

    for x1,y1 in coords:
        for x2,y2 in coords:
            if not  isUpperRight([x1,y1],[x2,y2]):
                continue
            upperCoordString=coordToString([x1,y2])
            rightCoordString=coordToString([x2,y1])
            if upperCoordString in coordsTable and rightCoordString in coordsTable:
                rectangleCount+=1

    return rectangleCount
def isUpperRight(coord1,coord2):
    x1,y1=coord1
    x2,y2=coord2
    return x2>x1 and y2>y1

def coordToString(coord):
    x,y=coord
    return str(x)+"-"+str(y)


if __name__=="__main__":
    coords = [
    [0, 0], [0, 1], [1, 1], [1, 0],
    [2, 1], [2, 0], [3, 1], [3, 0]]

    print(rectangleMania(coords))
