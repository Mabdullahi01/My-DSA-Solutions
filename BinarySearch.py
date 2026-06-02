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

'NeetCode 29'
'Search a 2D matrix'
'''Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.'''


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])

    top, bot = 0, m - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    if not (top <= bot):
        return False

    l, r = 0, n - 1

    while(l <= r):
        mid = (l + r) // 2
        if target < matrix[row][mid]:
            r = mid - 1
        elif target > matrix[row][mid]:
            l = mid + 1
        else:
            return True
    return False

#Time: O(logm + logn) = O(logmn)

'Or flattening the array, and completing it in one binary search'

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])

    l, r = 0, m * n - 1
    while l <= r:
        mid = (l + r) // 2
        row = mid // n
        col = mid % n

        val = matrix[row][col]

        if val == target:
            return True
        if val < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

#Time: O(logm + logn) = O(logmn)