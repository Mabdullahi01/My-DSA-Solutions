
'''Revision on Recursion'''

# def func(x):
#     if x >= 3:
#         return
#
#     print(x)
#     x += 1
#     func(x)
# func(1)

#
# def F(n):
#     if n <= 1:
#         return n
#     return F(n-1) + F(n-2)



"How it moves back up/ Backtracking"
# def func(i):
#     if i > 3
#         return
#     print(i)
#     func(i + 1)
#     print(f"End of call where i = {i}")
#     return
# func(1)

# def func(i, n):
#     if i > n:
#         return
#     print("Going down:", i)
#     print("Alchemy")
#     func((i + 1), n)
#     print("Coming back up:", i)
#     return
#
# func(1, 3)

"Backtracking"
# def func(i, n):
#     if i < 1:
#         return
#     func((i - 1), n)
#     print(i)
#
# N = int(input("In what range do you want to print N?"))
# func(N, N)

# def func(i, n):
#     if i < 1:
#         return
#
#     print(i)
#     func((i - 1), n)
#
#     return
# N = int(input("In what range do you want to print N?"))
# func(N, N)



"Parameterised Recursion"
'''Sum of first n numbers '''

# def func(i, sum = 0):
#     if i == 0:
#         return sum
#     return func(i - 1, sum + i)


# def func(n):
#     if n < 1:
#         return 0
#     return n + func(n - 1)
#
#
# n = int(input(f"Print the sum of the first N number? "))
# print(func(n))

'''Factorial of a number'''
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
# n = int(input(f"Print the sum of the first N number? "))
# print(fact(n))


'''Reverse an Array using Recursion'''

# def func(arr, i = 0):
#     n = len(arr)
#     if i >= (n//2):
#         return arr
#
#     arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
#     return func(arr, i + 1)



#Time: O(n) Space: O(n)

'''checking if a string is a palindrome'''

# def is_palindrome(s, i = 0):
#     n = len(s)
#     if i >= (n // 2):
#         return True
#     if s[i] != s[n - i - 1]:
#         return False
#     return is_palindrome(s, i + 1)

'''Multiple Recursion calls: Fibonacci'''

# def f(n):
#     if n <= 1:
#         return n
#     last = f(n - 1)
#     slast = f(n - 2)
#
#     return last + slast
# print(f(4))

# Time complexity is near 2^n

'''Level Order Traversal Implementation'''
# from collections import deque
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def level_order(root):
#     if not root:
#         return []
#
#     result = []
#     queue = deque([root])
#
#     while queue:
#         level = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             level.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         result.append(level)
#     return result
#
#
# root = TreeNode(1,
#         TreeNode(2, TreeNode(4), TreeNode(5)),
#         TreeNode(3, TreeNode(6), TreeNode(7)))
#
# print(level_order(root))

'''Pre-Order Traversal'''
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# def preorder(root):
#     if not root:
#         return
#     print(root.val)
#     preorder(root.left)
#     preorder(root.right)



'''Iterative Preorder'''
#
# # Root Left Right
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def preorder_iterative(root):
#     if not root:
#         return
#
#     stack = [root]
#
#     while stack:
#         node = stack.pop()
#         print(node.val, end=" ")
#
#         if node.right:
#             stack.append(node.right)
#
#         if node.left:
#             stack.append(node.left)
#
# root = TreeNode(1,
#         TreeNode(2, TreeNode(4), TreeNode(5)),
#         TreeNode(3, TreeNode(6), TreeNode(7)))
#
# preorder_iterative(root)

'''Iterative InOrder '''
#Left Root Right

# def inorder_iterative(root):
#     stack = []
#     curr = root
#
#     while True:
#         if curr is not None:
#             stack.append(curr)
#             curr = curr.left
#
#         else:
#             if not stack:
#                 break
#
#             curr = stack.pop()
#             print(curr.val, end=" ")
#
#             curr = curr.right

'''Iterative PostOrder'''

# Left Right Root
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def iterative_postorder(root):
#     stack = []
#     lastVisited = None
#     curr = root
#     result = []
#
#     while curr or stack:
#
#         while curr:
#             stack.append(curr)
#             curr = curr.left
#
#         peek = stack[-1]
#
#         if peek.right and lastVisited != peek.right:
#             curr = peek.right
#         else:
#             result.append(peek.val)
#             lastVisited = stack.pop()
#
#     return result
#
#
# root = TreeNode(1,
#         TreeNode(2, TreeNode(4), TreeNode(5)),
#         TreeNode(3))
#
# print(iterative_postorder(root))


'''Iterative In,Pre,Post Order Traversal, using a stack[(root, num)], where num can be 1 for pre, 2 for in, 3 for post'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def All_traversal(root):
    if not root:
        return [], [], []


    stack = [(root, 1)]
    pre_order = []
    in_order = []
    post_order = []

    while stack:
        node, state = stack.pop()

        if state == 1:
            pre_order.append(node.val)
            stack.append((node, 2))

            if node.left:
                stack.append((node.left, 1))


        elif state == 2:
            in_order.append(node.val)
            stack.append((node, 3))

            if node.right:
                stack.append((node.right, 1))

        else:
            post_order.append(node.val)

    return pre_order, in_order, post_order







'''Maximum depth of a binary Tree
Given the root of a binary tree, find the length of the longest path from the root to a leaf.'''

# Height will always be 1 + max(l, r)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if root is None:
        return 0
    lh = max_depth(root.left)
    rh = max_depth(root.right)

    return 1 + max(lh, rh)
# Time complexity O(N)
# Space complexity O(N)





'''Check for Balanced Binary Tree'''
'''This solution was built upon the maximum depth of binary tree solution, which enables us to keep a time complexity of O(N)'''

# The absolute Difference between left height and right height must be less or equal to 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    return balance_Check(root) != -1


def balance_Check(root):
    if root is None:
        return 0

    left_height = balance_Check(root.left)
    if left_height == -1: return -1

    right_height = balance_Check(root.right)
    if right_height == -1: return -1

    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)


# Time complexity is O(N)
# Space complexity is O(N)





'''Diameter of a Binary Tree'''

'''Given the root of a binary tree, return the length of the diameter of the tree.'''
'''The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
    This path may or may not pass through the root.'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def diameterOfBinaryTree(root):
    diameter = [0]  # using list as parameter
    height(root, diameter)
    return diameter[0]

def height(node, diameter):
    if node is None:
        return 0
    lh = height(node.left, diameter)
    rh = height(node.right, diameter)

    diameter[0] = max( diameter[0], lh + rh)

    return 1 + max(lh, rh)

'''OR using instance variable'''


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0  # Instance variable
        self.height(root)
        return self.diameter

    def height(self, node):
        if not node:
            return 0

        lh = self.height(node.left)
        rh = self.height(node.right)

        self.diameter = max(self.diameter, lh + rh)

        return 1 + max(lh, rh)


#Time complexity is O(N)
#Space complexity is O(h), where h is the height of the tree, in best case O(log n)


'''Maximum path sum of a binary tree'''

'''A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.maxValue = float('-inf')
        self.maxPathDown(root)
        return self.maxValue

    def maxPathDown(self, node):
        if node is None:
            return 0

        left_sum = max(0, self.maxPathDown(node.left)) # ignores negative nodes
        right_sum = max(0, self.maxPathDown(node.right)) # ignores negative nodes

        self.maxValue = max(self.maxValue, node.val + left_sum + right_sum)

        return node.val + max(left_sum, right_sum)

# class Solution:
#     def maxPathSum(self, root):
#         # Using list to hold max value (mutable container)
#         max_value = [float('-inf')]
#         self.maxPathDown(root, max_value)
#         return max_value[0]
#
#     def maxPathDown(self, node,max_value):
#         if node is None:
#             return 0
#
#         # Using max(0, ...) to ignore negative paths
#         left = max(0, self.maxPathDown(node.left, max_value))
#         right = max(0, self.maxPathDown(node.right, max_value))
#
#         max_value[0] = max(max_value[0], left + right + node.val)
#
#         return max(left, right) + node.val





'''Check for Identical Trees'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(rootp, rootq):
    if (rootp is None) or (rootq is None):
        return (rootp == rootq)

    return (rootp.val == rootq.val) and isSameTree(rootp.left, rootq.left) and isSameTree(rootp.right, rootq.right)




'''Binary Tree Zigzag Traversal'''
'''Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).'''


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        size = len(queue)
        row = [0] * size

        for i in range(size):
            node = queue.popleft()

            index = i if left_to_right else (size - 1 -i)

            row[index] = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(row)
        left_to_right = not left_to_right

    return result

# Time complexity is O(N)
# Space complexity is O(N)


'''Boundary of Binary Tree'''
'''The boundary of a binary tree is the concatenation of the root, the left boundary, 
the leaves ordered from left-to-right, and the reverse order of the right boundary.'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf(node):
    return node.left is None and node.right is None

def boundaryOfBinaryTree(root):
    res = []
    if not root:
        return res
    if not is_leaf(root):
        res.append(root.val)

    add_left_boundary(root, res)
    add_leaves(root, res)
    add_right_boundary(root, res)

    return res

def add_left_boundary(root, res):
    cur = root.left
    while(cur):
        if not is_leaf(cur):
            res.append(cur.val)
        if cur.left:
            cur = cur.left
        else:
            cur = cur.right

def add_right_boundary(root, res):
    cur = root.right
    tmp = []

    while cur:
        if not is_leaf(cur):
            tmp.append(cur.val)

        if cur.right:
            cur = cur.right
        else:
            cur = cur.left

    for i in range(len(tmp) - 1, -1, -1):
        res.append(tmp[i])

def add_leaves(root, res):
    if is_leaf(root):
        res.append(root.val)
        return

    if root.left:
        add_leaves(root.left, res)
    if root.right:
        add_leaves(root.right, res)



'NeetCode 46'
'Invert Binary Tree'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Approach
class DFS:

    def invertTree(self, root):
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# T : O(n), M : O(h) h is height of tree

# Queue, BFS solution

from collections import deque

class BFS:

    def invertTree(self, root):

        if not root:
            return None

        q = deque([root])

        while q:

            node = q.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return root
# T : O(n), M : O(n)


'NeetCode 47'
'Maximum depth of Binary Tree'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree():
    root = TreeNode(3)

    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root

class Recursive_DFS:
    def max_depth(self, root):
        if not root:
            return 0
        lh = self.max_depth(root.left)
        rh = self.max_depth(root.right)

        return 1 + max(lh,  rh)

class Iterative_BFS:
    def max_depth(self, root):
        if not root:
            return 0

        depth = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        return depth

class Iterative_DFS:
    def max_depth(self, root):
        if not root:
            return 0

        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

# T : O(n), M : O(n)

root = build_tree()


'NeetCode 48'
'Diameter of a binary tree'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.diameter


    def height(self, node):
        if not node:
            return 0

        lh = self.height(node.left)
        rh = self.height(node.right)

        self.diameter = max(self.diameter, rh + lh)

        return 1 + max(rh, lh)

# T : O(n), M : O(n)

'NeetCode 49'
'Balanced Binary Tree'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    return dfs_height(root) != -1


def dfs_height(root):
    if not root:
        return 0

    lh = dfs_height(root.left)
    if lh == -1: return -1

    rh = dfs_height(root.right)
    if rh == -1: return -1

    if abs(lh - rh) > 1: return -1

    return 1 + max(lh, rh)

# T: O(n), M: O(n)

'NeetCode 50'
'Same tree'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


'NeetCode 51'
'SubTree of another Tree'

class Solution:
    def isSubtree(self, s, t):
        if not t: return True
        if not s: return False

        if self.SameTree(s, t):
            return True
        return (self.isSubtree(s.left, t)) or (self.isSubtree(s.right, t))


    def SameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False

        return (self.SameTree(s.left, t.left)) and (self.SameTree(s.right, t.right))

# T: O(m * n) , M: O(m + n) if s has m nodes and t has n nodes

'NeetCode 52'
'Lowest common ancestor of a Binary search Tree'

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
# T : O(log n), M : O(1)

'NeetCode 53'
'Binary Tree Level Order Traversal BFS'
from collections import deque

class Solution:
    def levelOrder(self, root):
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            res.append(level)
        return res


# T : O(n), M : O(n)

'NeetCode 54'
'Binary Tree Right Side View'


class Solution:
    def rightSideView(self, root):
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res



# or enqueue the right child first
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionII:
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res

'NeetCode 55'
'Count Good Nodes in BT'

class Solution:
    def goodNodes(self, root):

        def dfs(node, maxVal):
            if not node:
                return 0
            # keep a count of the node that is greater than or equal to, the greatest so far
            count = 1 if node.val >= maxVal else 0
            # update the greatest so far
            maxVal = max(maxVal, node.val)
            left = dfs(node.left, maxVal)
            right = dfs(node.right, maxVal)
            return count + left + right

        return dfs(root, root.val)

# T : O(n), M : O( log n )

'NC 56'
'Validate Binary Search Tree'

class Solution:
    def isValidBST(self, root):

        def valid(node, minValue, maxValue):
            if not node:
                return True
            if not (node.val < maxValue and node.val > minValue):
                return False
            return (valid(node.left, minValue, node.val) and valid(node.right, node.val, maxValue))

        return valid(root, float("-inf"), float("inf"))

'NC 57'
'Kth smallest element in a BST'

# Iterative DFS
class Solution:
    def kthSmallest(self, root, k):
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

'NC 58'
'Construct Binary Tree from PreOrder and InOrder Traversal'

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1: ])

        return root



'Construct Binary Tree from PostOrder and InOrder Traversal'

class Solution:
    def buildTree(self, postorder, inorder):
        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(postorder[:mid], inorder[:mid])
        root.right = self.buildTree(postorder[mid:-1], inorder[mid + 1: ])

        return root


'NC 59'
'Binary Tree Maximum Path Sum'
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.maxi = float('-inf')
        self.maxPath(root)
        return self.maxi

    def maxPath(self, node):
        if not node:
            return 0

        left = max(0, self.maxPath(node.left))
        right = max(0, self.maxPath(node.right))

        self.maxi = max(self.maxi, left + right + node.val)

        return node.val + max(left, right)


'NC 60'
'Serialize and Deserialize BT'

class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("#")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)


    def deserialize(self, data):
        val = data.split(",")
        self.i = 0

        def dfs():
            if val[self.i] == "#":
                self.i += 1
                return None

            node = TreeNode(int(val[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

'NC 61'
'Implement Trie(Prefix Tree)'
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

'NC 62'
'Design Add and Search Words Data Structure'

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)


'LC 79'
'Word Search'

def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            word[i] != board[r][c] or
            (r, c) in path):
            return False

        path.add((r, c))
        res = (dfs(r + 1, c, i + 1) or # down
               dfs(r - 1, c, i + 1) or # up
               dfs(r, c + 1, i + 1) or # right
               dfs(r, c - 1, i + 1)) # left
        path.remove((r, c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
    return False













