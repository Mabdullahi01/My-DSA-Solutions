'''Given a string s, return true if it is a palindrome, false otherwise'''

#A string is a palindrome if it reads the same forward as backward

# def ifpalindrom(s):
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         if s[left] != s[right]:
#             return False
#
#         left += 1
#         right -= 1
#     return True
#
#
# print(ifpalindrom('aceba'))

'''Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).'''

# nums = [1, 2, 4, 6, 8, 9, 14, 15]
# target = 13
# def check_for_target(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left < right:
#         sum = nums[left] + nums[right]
#         if sum == target:
#             return True
#         if sum > target:
#             right -= 1
#         else:
#             left += 1
#     return False

'''Brute Force Solution,When the array is not sorted'''
#nums = [4, -2, 5, 0, 6, 3, 2, -1]
#target = -2
# def TwoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
# print(TwoSum([4, -2, 5, 0, 6, 3, 2, -1], -2))

'''Using Hashmap(Dictionaries)'''
# def TwoSum(nums, target):
#     hash = {}
#     for i in range(len(nums)):
#         num = nums[i]
#         complement = target - num
#         if complement in hash:
#             return [i, hash[complement]]
#
#         hash[num] = i
# print(TwoSum([4, -2, 5, 0, 6, 3, 2, -1], -2))
# Time: O(n)
# Space: O(n)


'''Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted'''
# arr1 = [1, 4, 7, 20]
# arr2 = [3, 5, 6]
# def Two_Sorted_Array(arr1, arr2):
#     arr = []
#     i = j = 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             arr.append(arr1[i])
#             i += 1
#         else:
#             arr.append(arr2[j])
#             j += 1
#     # If there are remaining element in arr1, append them
#     while i < len(arr1):
#         arr.append(arr1[i])
#         i += 1
#     #If there are remaining element in arr2, append them
#     while j < len(arr2):
#         arr.append(arr2[j])
#         j += 1
#     return arr
# print(Two_Sorted_Array([1, 2, 3, 7, 20], [3, 5, 6]))
# Time: O(n)
# Space: O(1)

#18th June
#Is Subsequence
#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# s = ace
# t = abcde
# def isSubsequence(s, t):
#     i = j = 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#
#     return i == len(s)
# print(isSubsequence('ace', 'abcde'))
# Time: O(n+m) where n is the length of s and m is the length of t
# Space: O(1)


#Write a function that reverses a string. The input string is given as an array of characters s.
#s = ["h", "e", "l", "l", "o"]

# def reverseString(s):
#     i = 0
#     j = len(s) - 1
#     while (i < j):
#         tmp = s[i]
#         s[i] = s[j]
#         s[j] = tmp
#         i += 1
#         j -= 1
#     return s
#
# print(reverseString(["H","a","n","n","a","h"]))


# def reverseString(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left, right = left + 1, right - 1
#     return s
#
# print(reverseString(["H","a","n","n","a","h"]))

'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order'''

# def sortedSquares(nums):
#     num = []
#     for i in nums:
#         num.append(i * i)
#     return sorted(num)
#
# print(sortedSquares([-4, -1, 0, 3, 10]))

# def sortedSquares(nums):
#     num = []
#     num = [i*i for i in nums]
#     return sorted(num)
# print(sortedSquares([-4, -1, 0, 3, 10]))


#Using two pointer
#nums = [-4, -1, 0, 3, 10]
# def sortedSquares(nums):
#     n = len(nums)
#     result = [0] * n
#     i = 0
#     j = n - 1
#     for k in range(n - 1, -1, -1):
#         if abs(nums[i]) > abs(nums[j]):
#             sqwr = nums[i]
#             i += 1
#         else:
#             sqwr = nums[j]
#             j -= 1
#         result[k] = sqwr * sqwr
#     return result
#
# print(sortedSquares([-4, -1, 0, 3, 10]))

#SLIDING WINDOW
#Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.


# def find_length(nums, k):
#     left = 0
#     curr = 0
#     ans = 0
#     for right in range(len(nums)):
#         curr += nums[right]
#         while curr > k:
#             curr -= nums[left]
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
#
# print(find_length([1, 2, 3, 4, 5], 7))

# Time : O(n)
# Space: O(1)


#You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

# def find_length(s):
#     left = curr = ans = 0
#     for right in range(len(s)):
#         if s[right] == "0":
#             curr += 1
#         while curr > 1:
#             if s[left] == "0":
#                 curr -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
#
# print(find_length("110101100"))

# Time : O(n) where n is the length of string s, as the workdone in each loop iteration is amortized constant
# space : O(1)



'''Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.'''
#nums = [10, 5, 2, 6]  k = 100
# def numSubarrayProductLessThanK(nums, k):
#     if k <= 1:
#         return 0
#     ans = left = 0
#     curr = 1
#     for right in range(len(nums)):
#         curr *= nums[right]
#         while curr >= k:
#             curr /= nums[left]
#             left += 1
#         ans += right - left + 1
#     return ans
#
# print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))

'''Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k'''

# def find_best_subarray(nums, k):
#     curr = 0
#     for i in range(k):
#         curr += nums[i]
#
#     ans = curr
#     for i in range(k, len(nums)):
#         curr += nums[i] - nums[i - k]
#         ans = max(ans, curr)
#
#     return ans
#
# print(find_best_subarray([1, 2, 3, 4, 5], 2))
# Time : O(n)
# Space: O(1)

'''You are given an integer array nums consisting of n elements, and an integer k, Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted'''


# nums = [1, 12, -5, -6, 50, 3]
# k = 4


# def findMaxAverage(nums, k):
#     curr = 0
#     for i in range(k):
#         curr += nums[i]
#         average = curr / k
#     ans = average
#     for i in range(k, len(nums)):
#         curr += nums[i]
#         curr -= nums[i - k]
#         average = curr / k
#         ans = max(ans, average)
#     return ans
# #We could just add return ans / k to the previous code and it's all solved
# print(findMaxAverage([5], 1))

'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.'''

#example nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

# def longestOnes(nums, k):
#     left = ans = curr = 0
#     for right in range(len(nums)):
#         if nums[right] == 0:
#             curr += 1
#         while curr > k:
#             if nums[left] == 0:
#                 curr -= 1
#             left += 1
#         ans = max(ans, right - left + 1)
#     return ans
# print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

'''Prefix sum'''
#Sum of subarray from i to j, is prefix[j] - prefix[i - 1] or prefix[j] - prefix[i] + nums[i]

'''Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.'''

# def answer_queries(nums, queries, limit):
#     prefix = [nums[0]]
#
#     for i in range(1, len(nums)):
#         prefix.append(nums[i] + prefix[-1])
#
#     ans = []
#     for x, y in queries:
#         curr = prefix[y] - prefix[x - 1]
#         ans.append(curr < limit)
#     return ans
#
# print(answer_queries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13 ))

# Time : O(n+m) where n is the length of nums and m is the queries length
# Space : O(n) space for building the prefix sum, My question, What of the space for building the ans array?

'''Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.'''
# nums = [10, 4, -8, 7]
# def waysToSplitArray(nums):
#     prefix = [nums[0]]
#     n = len(nums)
#     for i in range(1, n):
#         prefix.append(nums[i] + prefix[-1])
#     ans = 0
#     for i in range(n - 1):
#         left_section = prefix[i]
#         right_section = prefix[-1] - prefix[i]
#         if left_section >= right_section:
#             ans += 1
#     return ans
# Time : O(n)
# Space: O(n)
#
# def waysToSplitArray(nums):
#     left_section = 0
#     total = sum(nums)
#     ans = 0
#
#     for i in range( len(nums) - 1):
#         left_section += nums[i]
#         right_section = total - left_section
#         if left_section >= right_section:
#             ans += 1
#     return ans
# Time : O(n)
# Space: O(1)

'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.'''

# def runningSum(nums):
#     running = [nums[0]]
#     for i in range(1, len(nums)):
#         running.append(nums[i] + running[-1])
#     return running
# print(runningSum([3,1,2,10,1]))


'''Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

'''

# nums = [-3, 2, -3, 4, 2]
# prefix_sum = [-3, -1, -4, 0, 2]

# def minStartValue(nums):
#     prefix = [nums[0]]
#     n = len(nums)
#     for i in range(1, n):
#         prefix.append(nums[i] + prefix[-1])
#
#     min_prefix = min(prefix)
#     startValue = 1 - min_prefix
#     return max(startValue, 1)
#
#
# print(minStartValue([1,-2,-3]))


# def minStartValue(nums):
#     min_sum = float('inf')  # Initialize to positive infinity
#     curr_sum = 0
#
#     for num in nums:
#         curr_sum += num
#         min_sum = min(min_sum, curr_sum)
#
#     startValue = 1 - min_sum
#     return max(1, startValue)



# You are given a 0-indexed array nums of n integers, and an integer k.
#
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
#
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
#
# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
# nums = [7, 4, 3, 9, 1, 8, 5, 2, 6] k = 3
#PREFIX SUM SOLUTION
# prefixSum = [0, 7, 11, 14, 23, 24, 32, 37, 39, 45]
# def getAverages(nums, k):
#     n = len(nums)
#
#     avgs = [-1] * n
#     prefix = [0]
#
#     for i in range(n):
#         prefix.append(nums[i] + prefix[-1])
#
#     if k > n:
#         return -1
#     for i in range(k, n - k):
#         AvgSum = prefix[i + k + 1] - prefix[i - k]
#         avgs[i] = AvgSum // (2 * k + 1)
#     return avgs
# print(getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
# Time: O(n) two iterations of O(n) for the generation of both the prefix and avgs
# Space: O(n) output array avgs is not considered as an additional space, but the prefix array

#SLIDING WINDOW SOLUTION
# def getAverages(nums, k):
#     n = len(nums)
#     avgs = [-1] * n
#     window_sum = 0
#     window_size = 2 * k + 1
#
#     if window_size > n:
#         return avgs
#
#     for i in range(window_size):
#         window_sum += nums[i]
#     return window_sum
#
#     avgs[k] = window_sum // window_size
#
#     for i in range(k + 1, n - k):
#         window_sum += nums[i + k] - nums[i - k - 1]
#         avgs[i] = window_sum // window_size
#
#     return avgs
#
# nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
# k = 3
# print(getAverages(nums, k))
#
# Time: O(n)
# Space: O(1) avgs is not considered as extra space



#Bonus Problems
'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.'''
#s = "Let's take LeetCode contest"

# def reverseWords(s):
#     newstart = -1
#     ch_array = list(s)
#     n = len(s)
#
#     for i in range(n + 1):
#         if i == n or s[i] == " ":
#             start = newstart + 1
#             end = i - 1
#
#             while start < end:
#                 ch_array[start], ch_array[end] = ch_array[end], ch_array[start]
#                 start += 1
#                 end -= 1
#             newstart = i
#     return "".join(ch_array)
#
# s = "Let's take LeetCode contest"
# print(reverseWords(s))

#Bonus Problem
# Reverse Only Letters
'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.'''

#input: s = "ab-cd"
#output: "dc-ba"

# def ReverseOnlyLetters(s):
#     ans = []
#     j = len(s) - 1
#
#     for i, x in enumerate(s):
#         if x.isalpha():
#             while not s[j].isalpha():
#                 j -= 1
#             ans.append(s[j])
#             j -= 1
#         else:
#             ans.append(x)
#     return "".join(ans)
#
# print(ReverseOnlyLetters("Test1ng-Leet=code-Q!"))

'''Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
 If there is no common integer amongst nums1 and nums2, return -1.'''

# Input: nums1 = [1, 2, 3], nums2 = [2, 4]
# Output: 2
#BRUTE FORCE SOLUTION
# def getCommon(nums1, nums2):
#     for num1 in nums1:
#         for num2 in nums2:
#             if (num1 == num2):
#                 return num1
#     return -1
# print(getCommon([1, 2, 3, 4, 5], [1,3,5]))
#O(m * n) is the time complexity
#Space complexity is O(1)

#HASHSET solution

# def getCommon(nums1, nums2):
#     set1 = set(nums1)
#
#     for num in nums2:
#         if num in set1:
#             return num
#     return -1
# print(getCommon([2, 3, 4, 5], [1,3,5]))
#
# Time complexity: O(n + m), creating set1 takes O(n), checking elements in num2 takes O(m)
# Space complexity: O(n), initializing set1

# nums1 = [2, 4, 6, 8, 10]
# nums2 = [1, 1, 3, 4 , 10]
# def getCommon(nums1, nums2):
#     p = 0
#     q = 0
#     while(p < len(nums1) and q < len(nums2)):
#         if nums1[p] < nums2[q]:
#             p += 1
#         elif nums1[p] > nums2[q]:
#             q += 1
#         else:
#             return nums1[p]
#     return -1
# print(getCommon([2, 4, 6, 8, 10], [1, 1, 3, 4 , 10]))
#
# Time complexity: O(n + m)
# Space: O(1)

'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.'''

def plusOne(digits):
    n = len(digits)

    for i in range(n):
        idx = n - 1 - i

        if digits[idx] == 9:
            digits[idx] = 0

        else:
            digits[idx] += 1

            return digits

    return [1] + digits

'''Neetcode 1'''
'''Given an integer array nums, return true if any value appears at least twice in the array and return false if every element is distinct'''

# nums = [1, 2, 3, 1]  output: true

def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == nums[i]:
                return True
    return False
# Time complexity: O(n^2)
#Space complexity: O(1)

def containsDuplicate(nums):
    hashset = set()

    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False
# Time complexity: O(n)
#Space complexity: O(n)

'''NeetCode 2'''

''' Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''
# s = "anagram", t = "nagaram"

from collections import defaultdict

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    for i in s:
        dict1[i] += 1
        # if i in dict1:, we didn't need to perform this check because we're using defaultdict, we will if we use just an hashmap({})
        #     dict1[i] += 1
        # else:
        #     dict1[i] = 1
    for j in t:
        dict2[j] += 1

    return dict1 == dict2

# Time complexity is O(n+m), Two seperate loops for counting
# Space complexity is O(n) or O(1), At most 26keys in dictionary

'Using regular dict/ hashmap'
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    dict1 = {}
    dict2 = {}

    for i in s:
        dict1[i] = dict1.get(i, 0) + 1
    for j in t:
        dict2[j] = dict1.get(j, 0) + 1

    return dict1 == dict2

'Using single hashmap'

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    hashMap = {}

    for char in s:
        hashMap[char] = hashMap.get(char, 0) + 1

    for char in t:
        if char not in hashMap:
            return False
        hashMap[char] -= 1
        if hashMap[char] < 0:
            return False

    return True

#Time: O(n+m)
#Space: O(n), only one Hashmap


'Using Fixed Array size'

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    arr = [0] * 26

    for i in s:
        arr[ord(i) - ord('a')] += 1
    for i in t:
        arr[ord(i) - ord('a')] -= 1
        if arr[ord(i) - ord('a')] < 0:
            return False
    return True

# Time complexity is O(n)
# Space complexity is O(26)



'''NeetCode 6'''
'''Product of Array Except Self'''
'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].'''
# nums = [1, 2, 3, 4]
def productExceptSelf(nums):

        length = len(nums)

        Left, Right, answer = [0] * length, [0] * length, [0] * length

        Left[0] = 1
        for i in range(1, length):
            Left[i] = Left[i - 1] * nums[i - 1]

        Right[length - 1] = 1
        for i in range(length - 2, -1, -1):
            Right[i] = Right[i + 1] * nums[i + 1]

        for i in range(length):
            answer[i] = Left[i] * Right[i]

        return answer

# Time: O(n)
# Space: O(n)


'''Optimized solution'''

def productExceptSelf(nums):
    length = len(nums)
    answer = [1] * length

    for i in range(1, length):
        answer[i] = answer[i - 1] * nums[i - 1]

    Right = 1
    for i in range(length - 1, -1 , -1):
        answer[i] = answer[i] * Right
        Right *= nums[i]

    return answer



# Time: O(n)
# Space: O(1) auxilliary space


'''NeetCode 8'''

'''Encode and decode string
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.'''
#input :["Hello","World"]
# logic "5#Hello5#World, placing the length of the string at the start followed by a delimiter

def encode(givenstr):
    res = ""
    for s in givenstr:
        res += str(len(s)) + "#" + s
    return res

def decode(encodedstr):
    res, i = [], 0

    while i < len(encodedstr):
        j = i
        while encodedstr[j] != "#":
            j += 1
        length = int(encodedstr[i:j])
        res.append(encodedstr[1 + j: 1 + j + length])
        i = j + 1 + length
    return res

#Time: O(n)
#Space: O(k)


'''Neetcode 10'''

'''Valid palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise'''
#Input: s = "A man, a plan, a canal: Panama"
#Output: true


def isPalindrome(s):

    L, R = 0, len(s) - 1

    while L < R:
        while L < R and not alphaNum(s[L]):
            L += 1
        while R > L and not alphaNum(s[R]):
            R -= 1
        if s[L].lower() != s[R].lower():
            return False
        L, R = L + 1, R - 1
    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))


#Time: O(n)
#Space: O(1)




'''Given a string s, return true if it is a palindrome, false otherwise'''
#A string is a palindrome if it reads the same forward as backward
# s = aceca
def ifpalindrom(s):
    right = len(s) - 1
    left = 0
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


'''NeetCode 11'''

'''Two Sum II, with sorted input array
Given an array of integers that is already sorted in asecending order, find two numbers such that they add up to a specific target number.
Indices are not zero based'''

def twoSum(numbers, target):
    L, R = 0, len(numbers) - 1

    while L < R:
        currSum = numbers[L] + numbers[R]
        if currSum > target:
            R -= 1
        elif currSum < target:
            L += 1
        else:
            return [1 + L, 1 + R]


# Time: O(n)
# Space: O(1)


'''NeetCode 12'''
'''3Sum. Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.'''

def threeSum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        L, R = i + 1, len(nums) - 1
        while L < R:
            threeSum = a + nums[L] + nums[R]

            if threeSum > 0:
                R -= 1
            elif threeSum < 0:
                L += 1
            else:
                res.append([a, nums[L], nums[R]])
                L += 1
                while nums[L] == nums[L - 1] and L < R:
                    L += 1
    return res

# Time: O(n^2)
# Space: O(1)



'''NeetCode 13'''
'''Container with Most Water'''
'''You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.'''

'''Brute force solution'''
def maxArea(height):
    res = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
    return res
#Time: O(n^2)
#Space: O(1)



'''Two pointer Solution'''
def maxArea(height):
    L, R = 0, len(height) - 1
    res = 0

    while(L < R):
        area = min(height[L], height[R]) * (R - L)
        res = max(res, area)
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1
    return res

# Time: O(n)
# Space: O(1)


'''NeetCode 14'''
#hard
'''Trapping Rain Water'''
'''Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.'''

def trap(height):

    if not height: return 0
    L, R = 0, len(height) - 1
    res = 0

    leftMax, rightMax = height[L], height[R]

    while L < R:
        if leftMax < rightMax:
            L += 1
            leftMax = max(leftMax, height[L])
            res += leftMax - height[L]
        else:
            R -= 1
            rightMax = max(rightMax, height[R])
            res += rightMax - height[R]

    return res

#Time: O(n)
#space: O(1)


'''NeetCode 15'''
'''Best time to buy and sell stock'''
'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
'''

# prices = [7, 1, 5, 3, 6, 4]
'''Two Pointer Solution'''
def maxProfit(prices):
    L = 0 #buy
    R = 1 #sell
    maxP = 0

    while (R < len(prices)):
        if prices[L] > prices[R]:
            L = R
            R += 1
        else:
            profit = prices[R] - prices[L]
            maxP = max(maxP, profit)
            R += 1
    return maxP



'''Using One variable'''

def maxProfit(prices):

   minimum_price = float('inf')
   maxP = 0

   for price in prices:
       if price < minimum_price:
           minimum_price = price
       else:
           maxP = max(maxP, price - minimum_price)
   return maxP




#Time: O(n)
#Space: O(1)

"NeetCode 16"
'''Longest substring without repeating character'''
'''Given a string s, find the length of the longest substring without duplicate characters.'''

#input: s = "abcabcbb"
#Output: 3

#Input: s = "pwwkew"
#Output: 3


'Brute Force Solution'
def lengthOfLongestSubstring(s):
    max_length = 0
    for i in range(len(s)):
        unique_char = set()
        for j in range(i, len(s)):

            if s[j] in unique_char:
                break
            unique_char.add(s[j])
            max_length = max(max_length, j - i + 1)
    return max_length

# Time complexity is O(n^2)
# Space complexity is O(n)


'Sliding Window Solution'
def lengthOfLongestSubstring(s):

    hashmap = {}
    L = 0
    max_length = 0

    for R in range(len(s)):
        hashmap[s[R]] = hashmap.get(s[R], 0) + 1
        while hashmap[s[R]] > 1:
            hashmap[s[L]] -= 1

            if hashmap[s[L]] == 0:
                del hashmap[s[L]]
            L += 1

        max_length = max(max_length, R - L + 1)

    return max_length



# Time complexity is O(2n) = O(n) The right pointer iterate through the string once, and the while loop moves the left pointer only when needed, meaning each character is visited at most twice
# Space complexity is O(min(n,k)), where n is the number of unique characters, k is 26

"NeetCode 17"
'''Longest repeating character replacement'''
'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase
 English character. You can perform this operation at most k times.
 Return the length of the longest substring containing the same letter you can get after performing the above operations.'''

# Input: s = "ABABBA", k = 2
# Output: 5


'Sliding window technique'
def characterReplacement(s, k):
    hashmap = {}
    L = 0
    max_length = 0
    for R in range(len(s)):
        hashmap[s[R]] = hashmap.get(s[R], 0) + 1
        while((R - L + 1) - max(hashmap.values())) > k:
            hashmap[s[L]] -= 1
            L += 1
        max_length = max(max_length, R - L + 1)

    return max_length




# Time complexity : O(26n)
# Space complexity : O(26)


'More optimized sliding window'


def characterReplacement(s, k):
    hashmap = {}
    L = 0
    max_length = 0
    max_F = 0
    for R in range(len(s)):
        hashmap[s[R]] = hashmap.get(s[R], 0) + 1
        max_F = max(max_F, hashmap[s[R]])
        while((R - L + 1) - max_F) > k:
            hashmap[s[L]] -= 1
            L += 1
        max_length = max(max_length, R - L + 1)

    return max_length

'NeetCode 18'
'Permutation in string'
'''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2'''

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False

    s1_counts = [0] * 26
    s2_counts = [0] * 26

    for i in range(len(s1)):
        s1_counts[ord(s1[i]) - ord('a')] += 1
        s2_counts[ord(s2[i]) - ord('a')] += 1

    if s1_counts == s2_counts:
        return True

    for i in range(len(s1), len(s2)):
        s2_counts[ord(s2[i]) - ord('a')] += 1
        s2_counts[ord(s2[i - len(s1)]) - ord('a')] -= 1
        if s1_counts == s2_counts:
            return True
    return False












