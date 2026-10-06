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

#T: O(n^2) Iterating over the matrix to build the hashmap

'NC 80'
'Number of Islands'

'depth first search'
def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    Islands = 0
    visited = set()

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if grid[r][c] == "0":
            return
        if (r, c) in visited:
            return

        visited.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                Islands += 1
                dfs(r, c)
    return Islands
# T: O(m × n)
# M: O(m × n)

'Breadth first search'
from collections import deque

def NumIsland(grid):
    if not grid:
        return 0
    visited = set()
    Islands = 0
    rows, cols = len(grid), len(grid[0])

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited.add((r, c))

        while queue:
            r, c = queue.popleft()

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                r, c = r + dx, c + dy
                if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visited):
                    queue.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                Islands += 1
                bfs(r, c)
    return Islands

'LC 841'
'Keys and Rooms'

def canVisitAllRooms(rooms):
    seen = {0}
    def dfs(i):
        for neighbor in rooms[i]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)
    dfs(0)
    return len(seen) == len(rooms)

# T: O(N + E)
# M : O(N)

'NC 81'
'Clone Graph'

class Node:
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is None else []

def cloneGraph(node):
    oldToNew = {}
    def dfs(node):
        if not node:
            return None
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node)

'NC 90'
'Number of Connected Components in an Undirected Graph'

def countComponents(n, edges):

    seen = set()
    components = 0

    def dfs(node):
        for neighbor in Graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    Graph = defaultdict(list)
    for x, y in edges:
        Graph[x].append(y)
        Graph[y].append(x)

    for i in range(n):
        if i not in seen:
            seen.add(i)
            components += 1
            dfs(i)
    return components

# T: O(V + E)












