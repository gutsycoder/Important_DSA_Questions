#Lowest Common Manager
# You're given three inputs, all of which are instances of an OrgChart class that have a directReports property pointing to their direct reports.
# The first input is the top manager in an organizational chart (i.e., the only instance that isn't anybody else's direct report),
# and the other two inputs are reports in the organizational chart. The two reports are guaranteed to be distinct.
# Write a function that returns the lowest common manager to the two reports.
# topManager = Node A
# reportOne = Node E
# reportTwo = Node I
#       A
#     /   \
#    B      C
#   / \    /  \
#  D   E  F    G
# / \
# H  I
#OUTPUT: B
class OrgChart:
    def __init__(self,name):
        self.name=name
        self.directReports=[]
    def addDirectReports(self,directReports):
        for directReport in directReports:
            self.directReports.append(directReport)

def getLowestCommonManager(topManager, reportOne, reportTwo):
    if topManager==reportOne or topManager==reportTwo:
        return topManager
    lcm=None
    for i in topManager.directReports:
        temp=getLowestCommonManager(i,reportOne,reportTwo)
        if temp!=None:
            lcm=topManager if lcm else temp

    return lcm


if __name__=="__main__":
    orgCharts={}
    alphabets=["A","B","C","D","E","F","G","H","I"]
    for letter in alphabets:
        orgCharts[letter]=OrgChart(letter)
    orgCharts["A"].addDirectReports([orgCharts["B"], orgCharts["C"]])
    orgCharts["B"].addDirectReports([orgCharts["D"], orgCharts["E"]])
    orgCharts["C"].addDirectReports([orgCharts["F"], orgCharts["G"]])
    orgCharts["D"].addDirectReports([orgCharts["H"], orgCharts["I"]])
    print(getLowestCommonManager(orgCharts["A"],orgCharts["E"],orgCharts["I"]).name)
