from collections import defaultdict

def buildGraph(edges):

    Graph = defaultdict(list)
    for x, y in edges:
        Graph[x].append(y)
        Graph[y].append(x)
    return Graph

'LC 547'
'Number of Provinces'

def findCircleNum(isConnected):
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)


    n = len(isConnected)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    seen = set()
    province = 0

    for i in range(n):
        if i not in seen:
            province += 1
            seen.add(i)
            dfs(i)

    return province




