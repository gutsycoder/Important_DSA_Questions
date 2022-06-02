#POWERSETS / SUBSETS
#THE POWERSET P(X) OF A SET X IS THE SET OF ALL SUBSETS OF X. WRITE A FUNCTION THAT TAKES ARRAY OF UNIQUE INTEGERS
#AND RETURN IT'S POWERSET
# Sample Input
# array = [1, 2, 3]
# Sample Output
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

def powerset(arr):
    subsets=[[]]
    for ele in arr:
        for i in range(len(subsets)):
            currentSubset=subsets[i]
            subsets.append(currentSubset+[ele])
    return subsets




if __name__=="__main__":

    arr=[1,2,3]
    print(powerset(arr))
