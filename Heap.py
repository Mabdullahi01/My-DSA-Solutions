# from heapq import *
#
#
# heap = []
#
# heappush(heap, 1)
# heappush(heap, 2)
# heappush(heap, 3)
#
# heap[0], # outputs 1, as python implements min heap by default
# heappop(heap) # pop the min
#
# len(heap) # length of heap
#
# import heapq
# nums = [43, 2, 13, 634, 120]
# heapq.heapify(nums)
# # print(nums)
# # print(nums[0])
#
# heap = [67, 341, 234, -67, 12, -976]
# heapq.heapify(heap)
# heapq.heappush(heap, 7451)
# heapq.heappush(heap, -5352)
# print(heap)

# while heap:
    #print(heapq.heappop(heap))

'''Last Stone Weight'''
'''You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with x <= y'''

'''Array Based Simulation, Only good for when N < 30'''
def lastStoneWeight(stones):

    def remove_largest():
        index_of_largest = stones.index(max(stones))
        return stones.pop(index_of_largest)

    while len(stones) > 1:
        stone1 = remove_largest()
        stone2 = remove_largest()
        if stone1 != stone2:
            stones.append(stone1 - stone2)
    return stones[0] if stones else 0
# Time complexity is O(N^2)
# Space complexity is O(1)




'''Heap based simulation'''
import heapq

def lastStoneWeight(stones):

    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = abs(heapq.heappop(stones))
        second = abs(heapq.heappop(stones))
        if first != second:
            heapq.heappush(stones, -abs(first - second))

    return -stones[0] if stones else 0

# Time complexity: O(NlogN) converting the array into heap O(N) and doing two remmoves and one add on the heap takes O(logN)
# Space complexity: O(N), heapq.heapify() is an in place operation, but the heap still stores n elements



'''Minimum Operations to Halve Array sum'''
'''You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. 
Return the minimum number of operations to reduce the sum of nums by at least half..'''
# nums = [5, 19, 8, 1]
import heapq

def halveArray(nums):
    target = sum(nums) / 2
    ans = 0
    nums = [-num for num in nums]
    heapq.heapify(nums)

    while target > 0:
        ans += 1
        x = heapq.heappop(nums)
        target -= abs(x / 2)
        heapq.heappush(nums, x / 2)

    return ans

# Time complexity: O(NlogN)
# Space complexity: O(N)


'''Remove stones to Minimize the Total'''
'''You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. 
You should apply the following operation exactly k times:
Choose any piles[i] and remove floor(piles[i] / 2) stones from it.'''

#input: piles = [5,4,9], k = 2
#Output: 12
import heapq

def minStoneSum(piles, k):
    heap = [-pile for pile in piles]

    heapq.heapify(heap)

    while k > 0:
        maxheap = heapq.heappop(heap)
        heapq.heappush(heap, (maxheap // 2)) # This is because -9 // 2 directly rounds down to -5, so we don't need another subtraction operation
        k -= 1
    return -sum(heap)

#Time complexity: O(n + klogn)
#Space complexity: O(n)



'''Minimum Cost to Connect Sticks'''
'''You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.'''
'''You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. 
You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.'''
#Input: sticks = [2,4,3]
#Output: 14
# 2+3=5---[5,4], 5+4=9---[9]
# 5+9=14
import heapq

def connectSticks(sticks):
    heapq.heapify(sticks)
    cost = 0
    while (len(sticks) > 1):
        firstMin = heapq.heappop(sticks)
        SecondMin = heapq.heappop(sticks)
        cost += (firstMin + SecondMin)
        heapq.heappush(sticks, (firstMin + SecondMin))

    return cost

#Time complexity: O(NlogN)
#Space complexity: O(N)







'''NeetCode5'''
'''Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
#Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#Output: [1,2]


'''with Bucket Sort'''
def topKFrequent(nums, k):
    if k == len(nums):
        return nums

    hashMap = {}

    val = [[] for i in range(len(nums) + 1)]

    for key in nums:
        hashMap[key] = hashMap.get(key, 0) + 1

    for key, index in hashMap.items(): # The value here simply means 'index'
        val[index].append(key)

    res = []
    for i in range(len(val) - 1, 0, -1):
        for n in val[i]:
            res.append(n)
            if len(res) == k:
                return res


#Time complexity: O(n)
#Space complexity: O(n)



'''With Heap'''
from collections import Counter
import heapq

def topKFrequent(nums, k):

    counts = Counter(nums)
    heap = []


    for key, val in counts.items():
        heapq.heappush(heap, (val, key))
        if len(heap) > k:
            heapq.heappop(heap)

    return[pair[1] for pair in heap]



#Time complexity: O(n*logk) since the size of the heap never exceeds k
#Space complexity: O(n + k)



'''Find K closest Element'''

'''Given a sorted integer array arr, two integers k and x, return the k closest integers to x. 
The answer should also be sorted in ascending order. If there are ties, take the smaller elements.'''
#arr = [1, 4, 10, 15, 22] k = 3 x = 11

import heapq

def kClosestElement(arr, k, x):

    heap = []
    for num in arr:
        heapq.heappush(heap, (-abs(x - num), -num))

        if len(heap) > k:
            heapq.heappop(heap)

    return sorted([-pair[1] for pair in heap])



# Time: O(nlogk) + O(klogk) = O((n+k)logk)
# Space: O(k)


'''Kth largest element in an array'''
'''Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.'''
import heapq
def findKthLargest(nums, k):

    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

# Time: O(nlogk)
# Space: O(k)


'NC 64'
'Kth Largest Element in a Stream'


class KthLargest:

    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]



'Nc 65'
'Last Stone Weight'


'With Array'
def lastStoneWeight(stones):

    def largestStone():
        indexoflargest = stones.index(max(stones))
        return stones.pop(indexoflargest)

    while len(stones) > 1:
        y = largestStone()
        x = largestStone()
        if x != y:
            stones.append( y - x )
    return stones[0] if stones else 0

# T: O(n^2)
# M : O(1)


'with heap'

def lastStoneWeight(stones):
    stones = [-stone for stone in stones]

    heapq.heapify(stones)
    while len(stones) > 1:
        y = abs(heapq.heappop(stones))
        x = abs(heapq.heappop(stones))
        if y != x:
            heapq.heappush(stones, -(y - x))
    return -stones[0] if stones else 0

# T: O(nlogn)
# M : O(n)

'NC 66'
'K closest Point to Origin'

def KClosest(points, k):
    minHeap = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])

    heapq.heapify(minHeap)
    res = []
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1
    return res

# T: O(N + kLogN)
# M: O(N)




'''Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
#Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#Output: [1,2]


'''with Bucket Sort'''

def TopKFrequent(nums, k):
    if len(nums) == k:
        return nums

    values = [[] for i in range(len(nums) + 1)]
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
    # hashmap{num:freq}

    for value, freq in hashmap.items():
        values[freq].append(value)
    res = []

    for i in range(len(values) - 1, 0, -1):
        for  n in values[i]:
            res.append(n)
            if len(res) == k:
                return res

'with heap'

def TopKFrequent(nums, k):

    hashmap = {}
    Heap = []

    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
    for key, val in hashmap.items():
        heapq.heappush(Heap, (val, key))
        if len(Heap) > k:
            heapq.heappop(Heap)

    return [pair[1] for pair in Heap]
# T: O(n log k)
# M: O(n)

'NC 67'
'Kth Largest Element in an Array'

def findKthLargest(nums, k):

    minHeap = []

    for num in nums:
        heapq.heappush(minHeap, num)
        if len(minHeap) > k:
            heapq.heappop(minHeap)
    return minHeap[0]


# T: O(n log k)
# M: O(k)















