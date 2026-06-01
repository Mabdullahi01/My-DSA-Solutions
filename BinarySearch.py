## Binary Search

'Implementation'
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            #do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

'For left-most Duplicate Element'

def binary_search(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


'For right-most Duplicate Element'

def binary_search(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left - 1




'NeetCode 28'
'Binary Search'
'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.'''

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4

def search(nums, target):
    L, R = 0, len(nums) - 1

    while L <= R:
        M = (L + R) // 2 # or L + ((R - L) // 2) to avoid overflow

        if nums[M] > target:
            R = M - 1
        elif nums[M] < target:
            L = M + 1
        else:
            return M
    return -1

#Time: O(logn)
#Space: O(1)

