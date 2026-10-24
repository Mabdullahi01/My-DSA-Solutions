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
            row, col = queue.popleft()

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                r, c = row + dx, col + dy
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


'NC 82'
'Max Area of An Island'

def maxAreaOfIsland(grid):
    R, C = len(grid), len(grid[0])
    seen = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0 or (r, c) in seen:
            return 0
        seen.add((r, c))
        return (1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c))

    area = 0
    for r in range(R):
        for c in range(C):
            area = max(area, dfs(r, c))
    return area

'NC 83'
'Pacific Atlantic Water Flow'

def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        if ((r, c) in visit or r < 0 or c < 0 or
                r == ROWS or c == COLS or heights[r][c] < prevHeight):
            return
        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])

    return res

# T : O(R * C)

'NC 84'
'Surrounded Regions'


def solve(board):
    R, C = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r == R or c == C or board[r][c] != "O":
            return
        board[r][c] = "A"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # capture unsurrounded regions (O -> A)
    for r in range(R):
        for c in range(C):
            if board[r][c] == "O" and (r in [0, R - 1] or c in [0, C - 1]):
                dfs(r, c)

    # capture surrounded regions (O -> X)
    for r in range(R):
        for c in range(C):
            if board[r][c] == "O":
                board[r][c] = "X"

    # uncapture unsurrounded regions (A -> O)
    for r in range(R):
        for c in range(C):
            if board[r][c] == "A":
                board[r][c] = "O"

    return board

# T: O(R * C)


'NetWork Delay Time'
import heapq

def networkDelayTime(times, n, k):
    edges = defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))

    minHeap = [(0, k)]
    visit = set()
    t = 0

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = max(t, w1)

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, ((w2 + w1), n2))

    return t if len(visit) == n else -1

#T: O( E * log V)

'NC 85'
'Rotten Oranges'

def orangesRotting(grid):
    ROWS, COLS = len(grid), len(grid[0])
    fresh = 0
    q = deque()
    time = 0

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while q and fresh > 0:
        for i in range(len(q)):
            row, col = q.popleft()

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r < 0 or c < 0 or r >= len(grid) or
                        c >= len(grid[0]) or grid[r][c] != 1):
                    continue
                grid[r][c] = 2
                fresh -= 1
                q.append((r, c))
        time += 1

    return time if fresh == 0 else -1

#T : O( R * C)


'NC 86'
'Walls and Gates'

def wallsAndGates(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])
    visited = set()
    q = deque()

    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append((r, c))
                visited.add((r, c))
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    dist = 1
    while q:
        for i in range(len(q)):
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r < 0 or c < 0 or r >= ROWS or
                        c >= COLS or
                    rooms[r][c] == -1 or (r, c) in visited):
                    continue
                rooms[r][c] = dist
                q.append((r, c))
                visited.add((r, c))
        dist += 1

    return rooms

'Without the visited set'

def WallsAndGates(rooms):
    ROWS, COLS = len(rooms), len(rooms[0])
    q = deque()
    INF = 2147483647

    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append((r, c))
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    dist = 1
    while q:
        for i in range(len(q)):
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r < 0 or c < 0 or r >= ROWS or
                        c >= COLS or
                    rooms[r][c] != INF):
                    continue
                rooms[r][c] = dist
                q.append((r, c))
        dist += 1

    return rooms
#T : O( R * C)


'NC 87'
'Course Schedule I'

def canFinish(numCourses, prerequisites):
    Map = { i:[] for i in range(numCourses)}
    visited = set()

    for course, preq in prerequisites:
        Map[course].append(preq)

    def dfs(course):

        if Map[course] == []:
            return True
        if course in visited:
            return False

        visited.add(course)
        for pre in Map[course]:
            if not dfs(pre):
                return False
        visited.remove(course)
        Map[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True

# T : O( N + P)

'NC 88'
'Course Schedule II'

'with topological sort'

def findOrder(numCourses, prerequisites):
    cycle = set()
    completed = set()
    Order = []
    map = { i : [] for i in range(numCourses)}

    for x, y in prerequisites:
        map[x].append(y)

    def dfs(course):
        if course in completed:
            return True
        if course in cycle:
            return False
        cycle.add(course)

        for preq in map[course]:
            if not dfs(preq):
                return False

        cycle.remove(course)
        completed.add(course)
        Order.append(course)
        return True

    for course in range(numCourses):
        if dfs(course) == False:
            return []
    return Order

# T : O(V + E)

'NC 89'
'Redundant Connection'

'Union Find'
def findRedundantConnection(edges):
    parent = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(n):
        p = parent[n]

        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]

        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]

#T: O(N)


'NC 90'
'Number of Connected Components in an Undirected Graph'

'With Union Find'

def countComponent(n, edges):
    parents = [i for i in range(n)]
    rank = [1] * n

    def find(n1):
        p = parents[n1]

        while p != parents[p]:
            parents[p] = parents[parents[p]]
            p = parents[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            parents[p1] = p2
            rank[p2] += rank[p1]
        else:
            parents[p2] = p1
            rank[p1] += rank[p2]

        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res

# T: O(n + m) n nodes and m edges

'NC 91'
'Graph Valid Tree'

def validTree(n, edges):
    if not n:
        return True

    adj = { i : [] for i in range(n)}

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = set()

    def dfs(node, prev):
        if node in visited:
            return False
        visited.add(node)
        for j in adj[node]:
            if j == prev:
                continue
            if not dfs(j, node):
                return False
        return True
    return dfs(0, -1) and n == len(visited)

#T: O(V + E)

'NC 92'
'Word Ladder'

def ladderlength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    nei = defaultdict(list)
    wordList.append(beginWord)

    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            nei[pattern].append(word)

    visited = set([beginWord])
    q = deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visited:
                        visited.add(neiWord)
                        q.append(neiWord)
        res += 1
    return 0

# T: O( n^2 * m)

'NC 93'
'Reconstruct Itinerary'

def findItinerary(tickets):
    adj = { src : [] for src, dst in tickets}

    tickets.sort()
    for src, dst in tickets:
        adj[src].append(dst)

    res = ["JFK"]
    def dfs(src):
        if len(res) == len(tickets) + 1:
            return True
        if src not in adj:
            return False

        tmp = list(adj[src])
        for i, v in enumerate(tmp):
            adj[src].pop(i)
            res.append(v)

            if dfs(v): return True
            adj[src].insert(i, v)
            res.pop()
        return False

    dfs("JFK")
    return res


# T : O(E^2) E is the edge

"Hierholzer's Algorithm with Eulerian Path"

def findITinerary(tickets):
    adj = defaultdict(list)

    tickets.sort(reverse=True)
    for src, dst in tickets:
        adj[src].append(dst)

    route = []

    def dfs(src):
        while adj[src]:
            dst = adj[src].pop()
            dfs(dst)
        route.append(src)

    dfs("JFK")
    return route[::-1]

# Time : O(E log E) where E is the number of tickets
# M : O(E)
























