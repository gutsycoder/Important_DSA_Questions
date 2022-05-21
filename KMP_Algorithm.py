#KMP_Algorithm
# Write a function that take two strings and check if the first string contains the second one using the
# Knuth-Morris-Pratt Algorithm . The function should return a boolean.


def knuthMorrisPrattAlgorithm(string,pattern):
    lps=buildLPS(pattern)
    return doesMatch(string,pattern,lps)

def buildLPS(pattern):
    lps=[-1]*len(pattern)
    left,right=0,1
    while right<len(pattern):
        if pattern[left]==pattern[right]:
            lps[right]=left
            left+=1
            right+=1
        elif left>0:
            left=lps[left-1]+1
        else:
            right+=1
    return lps
def doesMatch(string,pattern,lps):
    i,j=0,0 #i refers to the string index and j refers to the pattern index

    while i+len(pattern)-j<=len(string): #checking whether there is enough letters left in the string to match
        if pattern[j]==string[i]:
            if j==len(pattern)-1:
                return True
            i+=1
            j+=1
        elif j>0:
            j=lps[j-1]+1
        else:
            i+=1
    return False














if __name__=="__main__":
    string="aefoaefcdaefcdaed"
    pattern="aefcdaed"
    print(knuthMorrisPrattAlgorithm(string,pattern))
