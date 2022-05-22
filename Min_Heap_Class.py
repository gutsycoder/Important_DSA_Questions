#Implement the Min_Heap CLass That Includes Building a Min_Heap from the input of array
#Inserting integers in the heap
#Removing heap's minimum/root value
#Peeking heap's minimum/root value
#Sifting integer up and down which is used for inserting and removing values
# array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
# // All operations below are performed sequentially.
# MinHeap(array): // instantiate a MinHeap (calls the buildHeap method a -
# buildHeap(array): [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
# insert(76): [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
# peek(): -5
# remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
# peek(): 2
# remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
# peek(): 6
# insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]

class MinHeap:

    def __init__(self,array):
        self.heap=self.buildHeap(array)  #O(n) time complexity

    def buildHeap(self,array):
        lastParentIdx=(len(array)-2)//2
        for currentIdx in reversed(range(lastParentIdx+1)):
            self.siftDown(currentIdx,array)
        return array

    def siftDown(self,currentIdx,heap):
        endIdx=len(heap)-1
        childOneIdx=2*currentIdx+1
        while childOneIdx<=endIdx:
            childTwoIdx=childOneIdx+1 if childOneIdx+1<=endIdx else -1
            if childTwoIdx!=-1 and  heap[childOneIdx]>heap[childTwoIdx]:
                idxToSwap=childTwoIdx
            else:
                idxToSwap=childOneIdx
            if heap[idxToSwap]<heap[currentIdx]:
                self.swap(currentIdx,idxToSwap,heap)
                currentIdx=idxToSwap
                childOneIdx=currentIdx*2+1
            else:
                return

    def siftUp(self,heap):
        currentIdx=len(heap)-1
        parentIdx=(currentIdx-1)//2
        while currentIdx>0 and heap[currentIdx]<heap[parentIdx]:
            self.swap(currentIdx,parentIdx,heap)
            currentIdx=parentIdx
            parentIdx=(currentIdx-1)//2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        valueToRemove=self.heap.pop()
        self.siftDown(0,self.heap)

        return valueToRemove

    def insert(self,value):
        self.heap.append(value)
        self.siftUp(self.heap)

    def swap(self,i,j,heap):
        heap[i],heap[j]=heap[j],heap[i]


if __name__=="__main__":
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    heap_obj=MinHeap(array)
    print(heap_obj.heap)
    heap_obj.insert(76)
    print(heap_obj.heap)
    heap_obj.peek()
    heap_obj.remove()
    print(heap_obj.heap)
    heap_obj.peek
    heap_obj.remove()
    print(heap_obj.heap)
    heap_obj.peek()
    heap_obj.insert(87)
    print(heap_obj.heap)
