#LIFO Last in, first out
# stack = []
#
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.pop()
# stack.pop()
# stack.pop()
#
# stack.append(-2)
# stack.append(0)
#
# if not stack:
#     print("Stack is empty")
# else:
#     print(f"Stack is not empty, top is : {stack[-1]}")

# VALID PARENTHESES
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# s = "()[]{}"

def isValid(s):
    stack = []
    hashmap = {"(":")", "{":"}", "[":"]"}

    for char in s:
        if char in hashmap:
            stack.append(char)
        else:
            if not stack:
                return False
            previous_check = stack.pop()
            if hashmap[previous_check] != char:
                return False
    return not stack

# print(isValid("()[]{}"))
#Time complexity is O(n)
#Space complexity is O(n) because the stack size can grow linearly with the input size

#REMOVE ALL ADJACENT DUPLICATE IN STRING
#s = "abbaca"

def removeDuplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
# print(removeDuplicates("leelcode"))

# Time complexity is O(n)
# Space complexity is O(n)

#BACKSPACE STRING COMPARE
# example s = "ab#c" and t = "ad#c" # represents a backspace

def backspaceCompare(s, t):
    def build(s):
        stack = []
        for char in s:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()
        return "".join(stack)

    return build(s) == build(t)
#
# print(backspaceCompare("ab#c", "ad#c"))


#SIMPLIFY PATH
#path = "/home/user/Documents/../Pictures"
def simplifyPath(path):
    stack = []

    for pth in path.split('/'):

        if pth == "..":
            if stack:
                stack.pop()
        elif pth == "." or pth == '':
            continue
        else:
            stack.append(pth)

    return '/' + '/'.join(stack)
#
# print(simplifyPath("/home/user/Documents/../Pictures"))
# Time is O(n)
# Space is O(n)


def simplifyPath(path):
    stack = []

    for pth in path.split('/'):
        if pth not in ['', '.', '..']:
            stack.append(pth)
        elif stack and pth == '..':
            stack.pop()
    return '/' + '/'.join(stack)
#
# print(simplifyPath("/home/user/Documents/../Pictures"))



#MAKE THE STRING GREAT
'Using iteration'
#s = leEeetcode
def makeGood(s):

    while len(s) > 1:

        find = False

        for i in range(len(s) - 1):
            curr_char, next_char = s[i], s[i + 1]
            if abs(ord(curr_char) - ord(next_char)) == 32:
                s = s[:i] + s[i + 2:]
                find = True
                break
        if not find:
            break

    return s
# print(makeGood("leEeetcode"))

# Time O(n^2)
# Space O(n) Because of the concatenation into a new string

'Using stack'

def makeGood(s):
    stack = []
    if len(s) < 2:
        return s
    for char in s:
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
# print(makeGood("leEeetcode"))
#
#
# Time complexity: O(n)
# Space complexity: O(n)

"QUEUE"

# from collections import deque
# queue = deque()
#
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# while queue:
#     print(queue.popleft())
#
# if not queue:
#     print("Queue is empty")

# queue.popleft()
# queue.popleft()

"Number Of Recent Calls"

# from collections import deque
#
# class RecentCounter:
#     def __init__(self):
#         self.queue = deque()
#
#     def ping(self, t):
#         while self.queue and self.queue[0] < t - 3000:
#             self.queue.popleft()
#         self.queue.append(t)
#         return len(self.queue)



# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         # return len(self.items) == 0
#         return not self.items
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#     def __str__(self):
#         return str(self.items)
#
#
#
# if __name__ == "__main__":
#     s = Stack()
#     s.push(10)
#     s.push(20)
#     s.push(30)
#
#     print("Top element:", s.peek())

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.top = None
#
#     def is_empty(self):
#         return self.top is None
#
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node
#         print(f"{data} pushed to stack")
#
#     def pop(self):
#         if self.is_empty():
#             print("Stack Underflow")
#             return None
#         popped_data = self.top.data
#         self.top = self.top.next
#         return popped_data
#
#     def peek(self):
#         if self.is_empty():
#             print("Empty Stack")
#             return None
#         return self.top.data
#
#     def display(self):
#         current = self.top
#         print("stack (top -> bottom): ", end="")
#
#         while current:
#             print(current.data, end="->")
#             current = current.next
#         print()
#
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.display()
#
# print("Top element:", s.peek())
# print("Popped element:", s.pop())
# s.display()

'NeetCode 21'
'Valid parentheses'
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid'''
# s = "()[]{}"

def isValid(s):
    stack = []
    hashmap = {"(":")", "{":"}", "[":"]"}

    for char in s:
        if char in hashmap: # opening bracket
            stack.append(char)
        else: # closing bracket
            if not stack:
                return False
            previous_check = stack.pop()
            if hashmap[previous_check] != char:
                return False
    return not stack


def isValid(s):
    stack = []
    hashmap = {"(":")", "{":"}", "[":"]"}

    for char in s:
        if char in hashmap: # opening bracket
            stack.append(char)
        else: # closing bracket
            if not stack or hashmap[stack[-1]] != char:
                return False
            stack.pop()
    return not stack
#Time complexity is O(n)
#Space complexity is O(n) because the stack size can grow linearly with the input size

'NeetCode 22'
'Design min stack'
'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.'''


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val )
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()

#Time: O(1) for the minstack operation


'NeetCode 23'
'Evaluate Reverse Polish Notation'

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

def evalRPN(tokens):
    stack = []

    for ch in tokens:
        if ch == '+':
            stack.append(stack.pop() + stack.pop())
        elif ch == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif ch == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif ch == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(ch))
    return stack[-1]

#Time: O(2n)
#Space: O(n)

'NeetCode 24'
'Generate Parentheses'
'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

'Backtracking approach'
def generateParenthesis(n):
    #only add open parenthesis if open < n
    #only add a closing parenthesis if open > closed
    #valid IIF open == closed == n
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    backtrack(0, 0)
    return res



#Time : O(4ⁿ / √n)
#Space: O(n)


'NeetCode 25'
'Daily temperature'
'''Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is
 the number of days you have to wait after the ith day to get a warmer temperature. 
 If there is no future day for which this is possible, keep answer[i] == 0 instead.'''

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
'BruteForce'

def dailytemperatures(temp):
    res = [0] * len(temp)

    for i in range(len(temp)):
        for j in range((i + 1, len(temp))):
            if temp[j] > temp[i]:
                res[i] = j - 1
                break # stop at first warmer temperature
    return res

#time: O(n²)
#space: O(n)


'Using stack'
def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = [] # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])
    return res

#time: O(n)
#space: O(n)


'Putting only the index on the stack'
def dailytemperatures(temperatures):
    res = [0]*len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append(i)
    return res

#time: O(n)
#space: O(n)






























