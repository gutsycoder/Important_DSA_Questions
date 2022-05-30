#AIRPORT CONNECTIONS PROBLEM
# For the purpose of this question, the phrases "airport route" and "airport connection" are used interchangeably.
# You're given a list of airports (three-letter codes like "JFK" ), a list of routes (one-way flights from one airport to another like ["JFK", "SFO"]), and a starting airport.
# Write a function that returns the minimum number of airport connections (one-way flights) that need to be added in order for someone to be able to reach any airport in the list, starting at the starting airport.
# Note that routes only allow you to fly in one direction; for instance, the route ["JFK", "SFO"] only allows you to fly from "JFK" to "SFO".
# Also note that the connections don't have to be direct; it's okay if an airport can only be reached from the starting airport by stopping at other airports first.
# Sample Input
# airports = [ "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO",
#"SIN", "TLV", "BUD"]
# routes [ =
# ["DSM", "ORD"],
# ["ORD", "BGI"],
# ["BGI", "LGA"],
# ["SIN", "CDG"], ["CDG", "SIN"],
# ["CDG", "BUD"],
# ["DEL", "DOH"],
# ["DEL", "CDG"],
# ["TLV", "DEL"],
# ["EWR", "HND"],
# ["HND", "ICN"],
# ["HND", "JFK"], ["ICN", "JFK"],
# ["JFK", "LGA"],
# ["EYW", "LHR"],
# ["LHR", "SFO"],
# ["SFO", "SAN"],
# ["SFO", "DSM"],
# ["SAN", "EYW"],
# startingAirport = "LGA"
#Sample Output
# 3 // ["LGA", "TLV"], ["LGA", "SFO"], and ["LGA", "EWR"]


class AirportNode:
    def __init__(self,airport):
        self.airport=airport
        self.isReachable=True
        self.connections=[]
        self.unreachableConnections=[]

def airportConnections(airports,routes,startingAirport):
    airportGraph=createAirportGraph(airports,routes)

    unreachableAirportNodes=getUnreachableAirportNodes(airportGraph,airports,startingAirport)

    markUnreachableConnections(airportGraph,unreachableAirportNodes)

    return getMinNumberOfNewConnections(airportGraph,unreachableAirportNodes)

def getMinNumberOfNewConnections(airportGraph,unreachableAirportNodes):
    numberOfConnections=0
    unreachableAirportNodes.sort(key=lambda airport: len(airport.unreachableConnections),reverse=True)
    for airport in unreachableAirportNodes:
        if airport.isReachable:
            continue
        numberOfConnections+=1
        for connection in airport.unreachableConnections:
            airportGraph[connection].isReachable=True
    return numberOfConnections



def markUnreachableConnections(airportGraph,unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport=airportNode.airport
        unreachableConnections=[]
        dfsAddUnreachableConnections(airportGraph,airport,unreachableConnections,{})
        airportNode.unreachableConnections=unreachableConnections


def dfsAddUnreachableConnections(airportGraph,airport,unreachableConnections,visitedAirports):
    if airport in visitedAirports or airportGraph[airport].isReachable:
        return
    visitedAirports[airport]=True
    unreachableConnections.append(airport)
    connections=airportGraph[airport].connections
    for connection in connections:
        dfsAddUnreachableConnections(airportGraph,connection,unreachableConnections,visitedAirports)







def getUnreachableAirportNodes(airportGraph,airports,startingAirport):
    visitedAirports={}
    dfsAirports(airportGraph,startingAirport,visitedAirports)
    unreachableAirportNodes=[]
    for airport in airports:
        if airport not in visitedAirports:
            unreachableAirportNodes.append(airportGraph[airport])
            airportGraph[airport].isReachable=False
    return unreachableAirportNodes

def dfsAirports(airportGraph,airport,visitedAirports):
    if airport in visitedAirports:
        return
    visitedAirports[airport]=True
    connections=airportGraph[airport].connections
    for connection in connections:
        dfsAirport(airportGraph,connection,visitedAirports)








def createAirportGraph(airports,routes):
    airportGraph={}
    for airport in airports:
        airportGraph[airport]=AirportNode(airport)
    for u,v in routes:
        airportGraph[u].connections.append(v)
    return airportGraph























if __name__=="__main__":

    airports = [ "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO",
    "SIN", "TLV", "BUD"]
    routes  =[
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"], ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"], ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]]
    startingAirport = "LGA"

    print(airportConnections(airports,routes,startingAirport))
