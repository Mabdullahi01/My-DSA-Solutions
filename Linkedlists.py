# def print_list(head):
#     curr = head
#     while curr:
#         print(curr.val, end=" -> ")
#         curr = curr.next
#     print("None")
#
#
# # Create: 1 -> 2 -> 3 -> 4 -> 5
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None  # make None as the default value for next.
#
#
# def count_nodes(head):
#     count = 1
#     current = head
#     while current.next is not None:
#         current = current.next
#         count += 1
#     return count
#
#
# nodeA = Node(6)
# nodeB = Node(3)
# nodeC = Node(4)
# nodeD = Node(2)
# nodeE = Node(1)
#
# nodeA.next = nodeB
# nodeB.next = nodeC
# nodeC.next = nodeD
# nodeD.next = nodeE
#
# print("This linked list's length is: (should print 5)")
# print(count_nodes(nodeA))






# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#
#         itr = self.head
#         llstr = ''
#
#         while itr:
#
#             llstr += str(itr.data) + '-->'
#             itr = itr.next
#         print(llstr)
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None)
#
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             itr = itr.next
#             count += 1
#         return count
#
#     def remove_at(self, index):
#         if index < 0 or index >= self.get_length():
#             raise Exception('Invalid index')
#
#         if index == 0:
#             self.head = self.head.next
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#
#             itr = itr.next
#             count += 1
#
#     def insert_at(self, index, data):
#         if index < 0 or index >= self.get_length():
#             raise Exception('Invalid index')
#
#         if index == 0:
#             node = Node(data, self.head)
#             self.head = node
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1
#
#
#
#
#
#
#
#
# ll = LinkedList()
# ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
# ll.print()
# ll.insert_at(2, 'apple')
# ll.print()
# print('length:', ll.get_length())





'''LEETCODE'''



# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# one = ListNode(1)
# two = ListNode(2)
# three = ListNode(3)
#
# one.next = two
# two.next = three
#
# head = one
# print(head.data)
# print(head.next.data)
# print(head.next.next.data)
#
#
#
# #TRAVERSAL
# def get_sum(head):
#     ans = 0
#     while head:
#         ans += head.data
#         head = head.next
#
#     return ans
# print(get_sum(one))

#RECURSIVE TRAVERSAL
# def get_sum(head):
#     if not head:
#         return 0
#
#     return head.data + get_sum(head.next)
#
# print(get_sum(one))

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# def add_node(prev_node, node_to_add):
#     node_to_add.next = prev_node.next
#     prev_node.next = node_to_add
#
# def print_list(head):
#     current = head
#     while current:
#         print(current.val, end = "-->")
#         current = current.next
#     print("None")
#
# one = ListNode(1)
# two = ListNode(2)
# three = ListNode(3)
#
# one.next = two
# two.next = three
# head = one
#
# print_list(head)
#
# new_node = ListNode(4)
# add_node(two, new_node)
# print_list(head)

# def delete_node(prev_node):
#     prev_node.next = prev_node.next.next
#
# delete_node(two)
# print_list(head)



"""Doubly Linked List"""

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
# # Let node be the node at position i
# def add_node(node, node_to_add):
#     prev_node = node.prev
#     node_to_add.next = node
#     node_to_add.prev = prev_node
#     prev_node.next = node_to_add
#     node.prev = node_to_add
# #Let node be the node at position i
# def delete_node(node):
#     prev_node = node.prev
#     next_node = node.next
#     if prev_node:
#         prev_node.next = next_node
#     if next_node:
#         next_node.prev = prev_node
#     node.next = None
#     node.prev = None
#
#
#
# def print_list_from_head(head):
#     current = head
#     while(current):
#         print(current.val, end = "<-->")
#         current = current.next
#     print("None")
#
# def print_list_from_tail(tail):
#     current = tail
#     while(current):
#         print(current.val, end = "<-->")
#         current = current.prev
#     print("None")
#
#
# head = ListNode(1)
# second = ListNode(2)
# third = ListNode(4)
#
# head.next = second
# second.prev = head
# second.next = third
# third.prev = second
#
# tail = third
# print_list_from_head(head)
#
#
# new_node = ListNode(3)
# add_node(third, new_node)
# print_list_from_head(head)
# print_list_from_tail(tail)
#
# delete_node(second)
# print_list_from_head(head)
# print_list_from_tail(tail)
#
# delete_node(third)
# print_list_from_head(head)
# #print_list_from_tail(tail)
#
# delete_node(head)
# head = head.next if head.next else None
# print_list_from_head(head)


'''Linked List with Sentinel Nodes'''


# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
#
# def add_to_end(node_to_add):
#     node_to_add.next = tail
#     node_to_add.prev = tail.prev
#     tail.prev.next = node_to_add
#     tail.prev = node_to_add
#
# def remove_from_end():
#     if head.next == tail:
#         return
#
#     node_to_remove = tail.prev
#     node_to_remove.prev.next = tail
#     tail.prev = node_to_remove.prev
#
# def add_to_start(node_to_add):
#     node_to_add.prev = head
#     node_to_add.next = head.next
#     head.next.prev = node_to_add
#     head.next = node_to_add
#
# def remove_from_start():
#     if head.next == tail:
#         return
#
#     node_to_remove = head.next
#     node_to_remove.next.prev = head
#     head.next = node_to_remove.next
#
# head = ListNode(None)
# tail = ListNode(None)
#
# head.next = tail
# tail.prev = head
#
# '''Dummy pointers '''
#
# def get_sum(head):
#     ans = 0
#     dummy = head
#     while dummy:
#         ans += dummy.val
#         dummy = dummy.next
#
#     return ans
#
# '''Exercise'''
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, val):
#         new_node = ListNode(val)
#         if not self.head:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#
#     def print_forward(self):
#         curr = self.head
#         while curr:
#             print(curr.val, end="<->" if curr.next else "\n")
#             curr = curr.next
#
#     def print_backward(self):
#         curr = self.tail
#         while curr:
#             print(curr.val, end="<->" if curr.prev else "\n")
#             curr = curr.prev
#
# exp = DoublyLinkedList()
# exp.append(1)
# exp.append(2)
# exp.append(3)
#
# exp.print_backward()

'''Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.'''


# def get_middle(head):
#     length = 0
#     dummy = head
#     while(dummy):
#         length += 1
#         dummy = dummy.next
#
#     for _ in range(length // 2):
#         head = head.next
#
#     return head.val

'''More efficient approach'''

# def get_middle(head):
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#
#     return slow.val


'''Given the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class LinkedList():
#     def hasCycle(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#
#         return False
#
# node4 = ListNode(4)
# node3 = ListNode(3, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)
#
# node4.next = node2
#
#
#
# Alch = LinkedList()
# print(Alch.hasCycle(node1))
#Time complexity: O(n)
#Space complexity: O(1)

'''Alternatelively'''

# def hasCycle(self, head):
#     seen = set()
#     while head:
#         if head in seen:
#             return True
#         seen.add(head)
#         head = head.next
#     return False

'''Given the head of a linked list and an integer k, return the kth node from the end.'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class LinkedList:
#     def find_node(self, head, k):
#         slow = head
#         fast = head
#
#         for _ in range(k):
#             fast = fast.next
#
#         while fast:
#             slow = slow.next
#             fast = fast.next
#         return slow.val
#
# node5 = ListNode(5)
# node4 = ListNode(4, node5)
# node3 = ListNode(3, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)
#
# Alch = LinkedList()
# print(Alch.find_node(node1, 2))

#Time complexity is O(n)
#Space complexity is O(1)

'''Or writing it this way, just learning different ways to test the code '''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def find_node(head, k):
#     slow = head
#     fast = head
#
#     for _ in range(k):
#         fast = fast.next
#
#     while fast:
#         slow = slow.next
#         fast = fast.next
#     return slow.val
#
# node5 = ListNode(5)
# node4 = ListNode(4, node5)
# node3 = ListNode(3, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)
#
#
# print(find_node(node1, 2))


'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def middleNode(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#
#         return slow.val
# Time complexity is O(n)
# Space complexity is O(1)

'''Alternatively'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class LinkedList:
#     def getMiddle(self, head):
#         length = 0
#         arr = []
#         while(head):
#             arr.append(head)
#             head = head.next
#             length += 1
#         return arr[length // 2].val

# Time complexity is O(n)
# Space complexity is O(1)


'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well'''

'''My solution, Not Good enough'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head):
#
#         dummy = head
#         unique_values = []
#         while dummy:
#             if dummy.val not in unique_values:
#                 unique_values.append(dummy.val)
#             dummy = dummy.next
#         return unique_values
# Time complexity is O(n)
# Space complexity is O(n)


'''Optimised Solution'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head):
#         current = head
#         while current and current.next:
#             if current.next.val == current.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#         return head
#
# def printLinkedList(head):
#     current = head
#     while current:
#         print(current.val, end=" → ")
#         current = current.next
#     print("None")
# node5 = ListNode(3)
# node4 = ListNode(1, node5)
# node3 = ListNode(1, node4)
# node2 = ListNode(1, node3)
# node1 = ListNode(1, node2)
#
# Alch = Solution()
# new_head = Alch.deleteDuplicates(node1)
#
# printLinkedList(new_head)

# Time complexity is O(n)
# Space complexity is O(1)

'''Reversing Linked List'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def reverse_list(head):
#     prev = None
#     curr = head
#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node
#
#     return prev
#
# node4 = ListNode(3)
# node3 = ListNode(2, node4)
# node2 = ListNode(1, node3)
# node1 = ListNode(0, node2)
#
# def print_(head):
#     current = head
#     while current:
#         print(current.val, end='-->')
#         current = current.next
#     print("None")
#
# print_(node1)
#
# new_head = reverse_list(node1)
# print("Reversed Linked List:  ")
# print_(new_head)


'''Swap Nodes In Pairs'''
# Input = A --> B --> C --> D
# Output = B --> A --> D --> C
'Recursive Approach'
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swap_pairs(self, head):
#         if not head or not head.next:
#             return head
#
#         first_node = head
#         second_node = head.next
#
#         first_node.next = self.swap_pairs(second_node.next)
#         second_node.next = first_node
#
#         return second_node
#
# node4 = ListNode('D')
# node3 = ListNode('C', node4)
# node2 = ListNode('B', node3)
# node1 = ListNode('A', node2)
#
# def print_list(head):
#     current = head
#     while current:
#         print(current.val, end='-->')
#         current = current.next
#     print("None")

# new_head = Solution().swap_pairs(node1)
# print_list(new_head)
# Time complexity is O(N)
# Space complexity is O(N) because of the stack space utilized for the recursion


'Iterative approach'
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def swap_pairs(self, head):
#         dummy = ListNode(0)
#         dummy.next = head
#         prev_node = dummy
#         while head and head.next:
#             first_node = head
#             second_node = head.next
#
#             prev_node.next = second_node
#             first_node.next = second_node.next
#             second_node.next = first_node
#
#
#             prev_node = first_node
#             head = first_node.next
#
#         return dummy.next
#
# node4 = ListNode('D')
# node3 = ListNode('C', node4)
# node2 = ListNode('B', node3)
# node1 = ListNode('A', node2)
#
# def print_list(head):
#     current = head
#     while current:
#         print(current.val, end='-->')
#         current = current.next
#     print("None")
#
# new_head = ListNode().swap_pairs(node1)
# print_list(new_head)

# Time complexity is O(N)
# Space complexity is O(1)

'''Maximum Twin Sum of a Linked List'''
'''Reversing Half of the Linked list Method'''
# head = [4, 2, 2, 3, 1, 5] output is 9
# Reversal from middle [4, 2, 2, 5, 1, 3]
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def PairSum(self, head):
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#
#
#         prev = None
#         while slow:
#             Next_node = slow.next
#             slow.next = prev
#             prev = slow
#             slow = Next_node
#
#         max_sum = 0
#         first_half = head
#         second_half = prev
#         while second_half:
#             twin_Sum = first_half.val + second_half.val
#             second_half = second_half.next
#             first_half = first_half.next
#             max_sum = max(max_sum, twin_Sum)
#         return max_sum
#
# node6 = ListNode(5)
# node5 = ListNode(1, node6)
# node4 = ListNode(3, node5)
# node3 = ListNode(2, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(4, node2)
#
# print(ListNode().PairSum(node1))

# Time complexity is O(N) Iterating over the linkedlist to find middle and reversing second half cost O(N)
# Iterating over half of the linked list also cost O(N) time, So overall time complexity is O(N)
# Space complexity is O(1), only few pointers were used

'''Using Array'''
# head = [4, 2, 2, 3, 1, 5] output is 9
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def PairSum(self, head):
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         n = len(arr)
#         max_sum = 0
#         for i in range(n // 2):
#             twin_sum = arr[i] + arr[n - i - 1]
#             max_sum = max(max_sum, twin_sum)
#         return max_sum
# node6 = ListNode(5)
# node5 = ListNode(1, node6)
# node4 = ListNode(3, node5)
# node3 = ListNode(2, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(4, node2)
#
# print(ListNode().PairSum(node1))

# Time: O(n) — One pass to fill array, one pass to compute twin sums
# Space: O(n) — For the array

'''Using while loop'''
# head = [4, 2, 2, 3, 1, 5] output is 9
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def PairSum(self, head):
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#
#         left = 0
#         right = len(arr) - 1
#         ans = 0
#         while(left < right):
#             ans = max(ans, arr[left] + arr[right])
#             left += 1
#             right -= 1
#         return ans

'''Reverse Linked List II'''
'''Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.'''
 #Input: head = [1,2,3,4,5], left = 2, right = 4
 #Output: [1,4,3,2,5]

 #1--->2--->3--->4---5

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def reverseBetween(head, left, right):
#     if not head or right == left:
#         return head
#     dummy = ListNode(0)
#     prev = dummy
#     dummy.next = head
#
#     for _ in range(left - 1):
#         prev = prev.next
#
#     curr = prev.next
#     tail = curr.next
#
#     for _ in range(right - left):
#         curr.next = tail.next
#         tail.next = prev.next
#         prev.next = tail
#         tail = curr.next
#
#     return dummy.next
#



'''Leetcode Solution'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def reverseBetween(head, left, right):
#     if not head or right == left:
#         return head
#     curr = head
#     prev = None
#     while left > 1:
#         prev = curr
#         curr = curr.next
#         left -= 1
#         right -= 1
#     cons = prev
#     tail = curr
#
#
#     while right:
#         Nextnode = curr.next
#         curr.next = prev
#         prev = curr
#         curr = Nextnode
#         right -= 1
#
#     cons.next = prev
#     tail.next = curr
#
#     return head


'''My Solution and What I can easily think about'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverseBetween(head, left, right):
#     if not head or right == left:
#         return head
#     dummy = ListNode(0)
#     prev = dummy
#     dummy.next = head
#     curr = head
#
#     for _ in range(left - 1):
#         prev = prev.next
#         curr = curr.next
#
#     cons = prev
#     tail = curr
#
#     for _ in range(right - left + 1):
#         Next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = Next_node
#
#
#     if cons:
#         cons.next = prev
#     else:
#         head = prev
#     tail.next = curr
#     return head


'''Recursive way of reversing a linkedlist'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head or not head.next:
        return head

    new_head = reverseList(head.next)

    head.next.next = head
    head.next = None

    return new_head





'NeetCode 35'
'Reverse Linked list'
'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''

'Iterative'
# 1 ---> 2 ---> 3 ---> 4 --->5
class ListNode:
    def __init__(self, val, next):
        self.next = next
        self.val = val

def reverseList(head):
    prev = None
    curr = head

    while curr:
        Nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = Nextnode

    return prev

def printList(head):
    curr = head

    while curr:
        print(curr.val, end="-->")
        curr = curr.next
    print("None")


node6 = ListNode(6, None)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# Iterative : T O(n) M O(1)


'Recursive'

def reverseList(head):
    if not head or not head.next:
        return head

    new_head = reverseList(head.next)

    head.next.next = head
    head.next = None

    return new_head

# Recursive : T O(n) M O(n)

'NeetCode 36'
'Merge Two Sorted Lists'
'''You are given the heads of two sorted linked lists list1 and list2.
'Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists'''

'Iteratively'

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2

    return dummy.next



'Recursively'

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    elif list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2



# Time complexity is O(m + n)
# Space complexity is O(m + n) due to recursive stack, as each function call adds a new frame



'NeetCode 37'
'ReOrder List'
'''You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reOrderList(head):

    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        next = second.next
        second.next = prev
        prev = second
        second = next

    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

    return first

# T: o(n), M : O(1)

'NeetCode 38'
'Remove Nth Node from end of List'

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # move right to nth node from head
    while n > 0 and right:
        right = right.next
        n -= 1

    # move left and right until right is at the end of the list
    while right:
        left = left.next
        right = right.next

    # delete the nth node
    left.next = left.next.next

    return dummy.next

# T: o(n), M : O(1)

























































































