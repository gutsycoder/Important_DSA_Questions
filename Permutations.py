#PERMUTATIONS
#Write a functionthat takes array of unique integers and returns an array of all permutations of  those integers in the array
#in no particular order
#Sample Input [1,2,3]
#Sample Output [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def getPermutations(array):
    permutations=[]
    getPermutationsHelper(0,array,permutations)

    return permutations

def getPermutationsHelper(i,array,permutations):
    if i==len(array)-1:
        permutations.append(array[:])
        return

    for j in range(i,len(array)):
        array[i],array[j]=array[j],array[i]
        getPermutationsHelper(i+1,array,permutations)
        array[j],array[i]=array[i],array[j]
        









if __name__=="__main__":
    array=[1,2,3]
    print(getPermutations(array))
