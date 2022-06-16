#INTERLEAVING STRING
# Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by
# interweaving the first two strings.
# To interweave strings means to merge them by alternating their letters without any specific pattern.
# For instance, the strings "abc" and "123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23" (this list is nonexhaustive).
# Letters within a string must maintain their relative ordering in the interwoven string.
# Sample Input
# one = "algoexpert"
# two = "your-dream-job"
# three="your-algodream-expertjob"
# Sample Output
# true

def interweavingStrings(one, two, three):
    if (len(one)+len(two))!=len(three):
        return False
    cache=[[None for j in range(len(two)+1)]for i in range(len(one)+1)]
    return isInterleave(one,two,three,0,0,cache)

def isInterleave(one,two,three,i,j,cache):
    k=i+j
    if cache[i][j]:
        return cache[i][j]
    if k==len(three):
        return True
    if i<len(one) and one[i]==three[k]:
        cache[i][j]=isInterleave(one,two,three,i+1,j,cache)
        if cache[i][j]:
            return True
    if j<len(two) and two[j]==three[k]:
        cache[i][j]=isInterleave(one,two,three,i,j+1,cache)
        return cache[i][j]
    cache[i][j]=False
    return cache[i][j]





if __name__=="__main__":
    one="algoexpert"
    two="your-dream-job"
    three="your-algodream-expertjob"
    print(interweavingStrings(one,two,three))
