# Given an undirected graph represented as an adjacency matrix and an integer k,
# write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices
# share the same color using at most k colors.


def canColor(adjMat, k):
    numNodes = len(adjMat)
    if numNodes <= k:
        return True
    nodes = {i: None for i in range(numNodes)}
    colors = [i for i in range(k)]
    # sort by number of neighbors
    nodeKeys = sorted(nodes.keys(), key=lambda a: sum(adjMat[a]), reverse=True)
    for nodeKey in nodeKeys:
        row = adjMat[nodeKey]
        excludeColors = []
        for neighbIdx in range(len(row)):
            if row[neighbIdx] == 1 and nodes[neighbIdx] != None and neighbIdx != nodeKey:
                excludeColors.append(nodes[neighbIdx])
        if len(excludeColors) == len(colors):
            return False
        for color in colors:
            if color not in excludeColors:
                nodes[nodeKey] = color

    return True

graph1 = [[1,1,0], [1,1,1], [0,1,1]]

print(canColor(graph1, 1) == False)
print(canColor(graph1, 2) == True)

graph2 = [[1,1,1], [1,1,1], [1,1,1]]

print(canColor(graph2, 2) == False)
print(canColor(graph2, 3) == True)