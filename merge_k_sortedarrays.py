# Merge Sorted Arrays
# Write a function that takes in a non-empty list of non-empty sorted arrays of integers and
# returns a merged list of all of those arrays.
# The integers in the merged list should be in sorted order.
# Sample Input
# arrays = [
# [1, 5, 9, 21],
# [-1, 0],
# [-124, 81, 121],
# [3, 6, 12, 20, 150]]
# Sample Output
# [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
import heapq
def mergeSortedArrays(arrays):
    heap=[]
    sortedList=[]
    for i in range(len(arrays)):
        heapq.heappush(heap,(arrays[i][0],i,0))

    while heap:
        smallest,arrayNumber,idx=heapq.heappop(heap)
        sortedList.append(smallest)
        if idx==len(arrays[arrayNumber])-1:
            continue
        heapq.heappush(heap,(arrays[arrayNumber][idx+1],arrayNumber,idx+1))
    return sortedList

if __name__=="__main__":
    arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150]]
    print(mergeSortedArrays(arrays))
