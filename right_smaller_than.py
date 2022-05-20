#RIGHT SMALLER THAN QUESTION

# Write a function that takes in an array of integers and returns an array of the same length,
# where each element in the output array corresponds to the number of integers in the input array
# that are to the right of the relevant index and that are strictly smaller than the integer at that index.
# In other words, the value at output[i] represents the number of integers that are to the right of i and that are strictly smaller than input[i].
#Input=[8,5,11-1,3,4,2] Output =[5,4,4,0,1,1,0]

def rightsmallerthan(array):

    def merge(left,right):
        aux=[]
        l,r,count=0,0,0
        while l<len(left) and r<len(right):
            if left[l][1]>right[r][1]:
                aux.append(right[r])
                count+=1
                r+=1
            else:
                aux.append(left[l])
                res[left[l][0]]+=count
                l+=1
        while l<len(left):
            aux.append(left[l])
            res[left[l][0]]+=count
            l+=1
        while r<len(right):
            aux.append(right[r])
            r+=1
        return aux



    def merge_sort(info):
        if len(info)<=1:
            return info
        mid=len(info)//2
        left=merge_sort(info[:mid])
        right=merge_sort(info[mid:])
        return merge(left,right)
    res=[0]*len(array)
    info=[]
    for index,value in enumerate(array):
        info.append((index,value))
    merge_sort(info)
    print(res)






if __name__=="__main__":
    array=[8,5,11,-1,3,4,2]
    print(rightsmallerthan(array))
