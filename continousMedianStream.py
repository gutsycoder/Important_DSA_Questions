# Continuous Median
# Write a ContinuousMedianHandler class that supports:
# The continuous insertion of numbers with the insert method.
# The instant (O(1) time) retrieval of the median of the numbers that have been inserted thus far with the getMedian method.
# The getMedian method has already been written for you. You simply have to write the insert method.
# The median of a set of numbers is the "middle" number when the numbers are ordered from smallest to greatest.
# If there's an odd number of numbers in the set, as in {1, 3, 7}, the median is the number in the middle ( 3 in this case);
# if there's an even number of numbers in the set, as in {1, 3, 7, 8}, the median is the average of
# the two middle numbers ( (3 + 7) / 2 == 5 in this case).
# Sample Usage
# // All operations below are performed sequentially.
# ContinuousMedianHandler(): // instantiate a ContinuousMedianHandler
# insert(5): -
# insert(10):
# getMedian(): 7.5
# insert(100):
# getMedian(): 10
# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
from heapq import *
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.heap=Heap()
        self.median = None

    def insert(self, number):
        if len(self.heap.low)==len(self.heap.high):
            heappush(self.heap.high,-heappushpop(self.heap.low,-number))
        else:
            heappush(self.heap.low,-heappushpop(self.heap.high,number))


    def getMedian(self):
        if len(self.heap.low)==len(self.heap.high):
            self.median=(self.heap.high[0]-self.heap.low[0])/2
        else:
            self.median=(self.heap.high[0])
        return self.median
class Heap:
    def __init__(self):
        self.low=[]
        self.high=[]

if __name__=="__main__":
    obj=ContinuousMedianHandler()
    obj.insert(5)
    obj.insert(10)
    print(obj.getMedian())
    obj.insert(100)
    print(obj.getMedian())
