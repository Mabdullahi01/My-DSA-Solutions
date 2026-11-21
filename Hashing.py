# hash_map = {1: 2, 5: 3, 7: 2}
# print(hash_map[5])
# print(1 in hash_map)
# print(2 in hash_map)
# hash_map[5] = 6
# hash_map[9] = 15
# print(hash_map)

#del hash_map[9]
#hash_map.pop(5)
#print(len(hash_map))

# for key in hash_map.keys():
#     print(key)

# for value in hash_map.values():
#     print(value)

#my_hash_map = { }

#my_hash_map[4] = 83
#print(my_hash_map)
#print(4 in my_hash_map)
#print(854 in my_hash_map)

#my_hash_map[8] = 327
#my_hash_map[45] = 82523
#print(my_hash_map)

# for key, value in my_hash_map.items():
#     print(f"{key}: {value}")


#Two Sum
# nums = [5, 2, 7, 10, 3, 9]
# target = 8

def twoSum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in hash_map:
            return [i, hash_map[comp]]
        hash_map[nums[i]] = i
    return [-1, -1]
#
# nums = [4, -2, 5, 0, 6, 3, 2, -1]
# target = -2
# print(twoSum(nums, target))
# Time: O(n)
# Space: O(n) because the number of keys the hashmap will store scales linearly with the input size

'''Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.'''
# s = 'swiss'
def repeatedCharacter(s):
    for i in range(len(s)):
        c = s[i]
        for j in range(i):
            if s[j] == c:
                return c
    return " "
# s = 'swiss'
# print(repeatedCharacter(s))

#Approach 2, Using HashSet
def repeatedCharacter(s):
    seen = set()
    for i in s:
        if i in seen:
            return i
        seen.add(i)
    return ""
# s = 'abcdeda'
# print(repeatedCharacter(s))

#Time complexity is O(n) as each loop iterations runs in constant time, While the space complexity is O(1), Because the input can only have
#characters from the exchange alphabet, But it could also be O(m) where m is the number of allowable charcters in the input

'''Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums'''

def find_numbers(nums):
    ans = []
    nums_set = set(nums)
    for x in nums_set:
        if (x + 1 not in nums_set and x - 1 not in nums_set):
            ans.append(x)
    return ans
# nums = [1, 2, 3, 5, 6, 7, 9]
# print(find_numbers(nums))

# Time Complexity is O(n), Because of the conversion of the list to set. The not in operation for list has a time complexity of O(n)
# which would make the time complexity to be O(n^2) if the list isn't converted to set
# The set Occupies O(n) space



# print(chr(ord('a') + 0)) # Output a
# print(chr(ord('a') + 1)) # Output b
# print(chr(97)) # Output a
# print(ord('z')) # Output 122



'''A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.'''

#Approach1

def checkIfPangram(sentence):
    for i in range(26):
        curr_char = chr(ord('a') + i)
        if sentence.find(curr_char) == -1:
            return False
    return True
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# print(checkIfPangram(sentence))
#Time complexity is O(n) and the Space is O(1)

#Approach2 Using HASH SET

def checkIfPangram(sentence):
    seen = set(sentence)
    return len(seen) == 26
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# print(checkIfPangram(sentence))

# Time complexity is O(N)
# Space complexity is O(1) Because the hash set can only contain at most 26 unique lowercase letters

'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''

def missingNumber(nums):
    n = len(nums)
    curr = 0
    for i in range(n):
        curr += nums[i]
    rangesum = sum(range(0, n+1))
    return (rangesum - curr)
# nums = [0,1]
# print(missingNumber(nums))
# Time: O(n)
# Space:O(n) Because of the rangesum that store the sum of the range(0, n+1) numbers

#Optimized Code
def missingNumber(nums):
    n = len(nums)
    curr = 0
    for i in range(n):
        curr += nums[i]
    rangesum = (n * ( n + 1)) // 2
    return (rangesum - curr)
# nums = [0,1]
# print(missingNumber(nums))
# Time: O(n)
# Space: O(1)

'''Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.'''
#Approach 1
# def countElements(arr):
#     count = 0
#     for x in arr:   #O(n)
#         if (x + 1) in arr: #O(n)
#             count += 1
#     return count
#
# arr = [1,1,3,3,5,5,7,7]
# print(countElements(arr))
# Time: O(n^2)
# Space: O(1)

#Approach 2, Using HashSet

# def countElements(arr):
#     hashset = set(arr) #O(n)
#     count = 0
#     for x in arr: #O(n)
#         if x + 1 in hashset: #O(1)
#             count += 1
#     return count
# arr = [1,1,3,3,5,5,7,7]
# print(countElements(arr))

# Time: O(n)
# Space: O(n), because hashset needs to store each unique integer from arr

#COUNTING
'''You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.'''

from collections import defaultdict
# s = eceba k = 2
# def find_longest_substring(s, k):
#     counts = defaultdict(int)
#     ans = left = 0
#     for right in range(len(s)):
#         counts[s[right]] += 1
#         while len(counts) > k:
#             counts[s[left]] -= 1
#
#             if counts[s[left]] == 0:
#                 del counts[s[left]]
#             left += 1
#         ans =  max(ans, right -left + 1)
#      return ans
# s = 'eceba'
# k = 2
# print(find_longest_substring(s, k))
# Time: O(n)
# Space: O(k) The hashmap occupies O(k) space, as the algorithm will delete elements from the hash map once it grows beyond k


'''Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.'''
#nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
# from collections import defaultdict
#
# def Intersection(nums):
#     counts = defaultdict(int)
#     for arr in nums:
#         for x in arr:
#             counts[x] += 1  # To populate the hashmap,it cost O(n.m) to iterate over all elements
#
#     n = len(nums)
#     ans = []
#     for key, value in counts.items(): # O(n.m), Iterates over all unique elements
#         if value == n:
#             ans.append(key)
#     return sorted(ans)  # O(mlogm)
#
# nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
# print(Intersection(nums))
# Lets say there are n lists and each list has an average of m elements
#Time: O(n.m + m.logm) = O(m.(n + logm))
#space: O(n.m), hashmap will grow to a size of n.m


'''Given a string s, determine if all characters have the same frequency.'''

# from collections import defaultdict
# #s = abacbc
# def areOccurrenciesEqual(s):
#     counts = defaultdict(int)
#     for i in s:
#         counts[i] += 1
#     frequencies = counts.values()
#     frequency = set(frequencies)
#
#     return len(frequency) == 1
# print(areOccurrenciesEqual('abacbc'))

# Time: O(n),  It cost O(n) to populate the hashmap, and O(n) to convert the hashmap to set, Which gives total of O(n)
# Space: O(k), The space that the hashmap and set will occupy is equal to the number of unique characters.where k is the number of characters that
# could be in the input, which is 26 in this problem, O(26) = O(1)


'''Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.'''
# nums = [-2, 1, 2, -2, 5, -2, 1] k = 3
# prefixsum = [-2, -1, 1, -1, 4, 2, 3]
#
# from collections import defaultdict
#
# def subarraySum(nums, k):
#     hashmap = defaultdict(int)
#     hashmap[0] = 1
#     ans = curr = 0
#     for num in nums:
#         curr += num
#         ans += hashmap[curr - k]
#         hashmap[curr] += 1
#     return ans
# nums = [-2, 1, 2, -2, 5, -2, 1]
# k = 3
# print(subarraySum(nums, k))
# #Time and Space complexity of this Algorithm is O(n)



'''Given an array of positive integers nums and an integer k. Find the number of subarrays with exactly k odd numbers in them.'''

from collections import defaultdict

# def numberOfSubarrays(nums, k):
#     hashmap = defaultdict(int)
#     hashmap[0] = 1
#     ans = curr = 0
#
#     for num in nums:
#         curr += num % 2
#         ans += hashmap[curr - k]
#         hashmap[curr] += 1
#     return ans
# nums = [1, 1, 2, 1, 1]
# k = 3
# print(numberOfSubarrays(nums, k))

# Time And Space complexity is O(n)


'''You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.'''

#USING HASHSET
# def findWinners(matches):
#     one_loss = set()
#     zero_loss = set()
#     more_loss = set()
#
#     for winner, loser in matches:
#         if (winner not in one_loss) and (winner not in more_loss):
#             zero_loss.add(winner)
#         if loser in zero_loss:
#             zero_loss.remove(loser)
#             one_loss.add(loser)
#         elif loser in one_loss:
#             one_loss.remove(loser)
#             more_loss.add(loser)
#         # elif loser in more_loss: #Without these two lines, This code will still function correctly and the output will be the same, but it helps
#         #     continue             # to avoid redundant processing and it helps optimize the code because it avoid re-adding of loser to the more_loss
#         else:                      # set
#             one_loss.add(loser)
#     return [sorted(zero_loss), sorted(one_loss)]
#
# print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

# Time complexity: O(nlogn)
# Space: O(n)

#USING HASHMAP
#matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

# def findWinners(matches):
#     losses = {}
#
#     for winner, loser in matches:
#         losses[winner] = losses.get(winner, 0)
#         losses[loser] = losses.get(loser, 0) + 1
#
#         zero_loss = []
#         one_loss = []
#     for player, count in losses.items():
#         if count == 0:
#             zero_loss.append(player)
#         if count == 1:
#             one_loss.append(player)
#     return [sorted(zero_loss), sorted(one_loss)]
#
# print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

#Time: O(nlogn)
#Space: O(n)

'''Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.'''
# nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
#
# def largestUniqueNumber(nums):
#     hashmap = {}
#     for num in nums:
#         if num in hashmap:
#             hashmap[num] += 1
#         else:
#             hashmap[num] = 1
#
#     ans = 0
#     for key, value in hashmap.items():
#         if value == 1:
#             ans = max(ans, key)
#     return ans
#
#
# print(largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))
# # Space: O(n)
# # Time: O(n)

#DIFFRENT METHOD OF FILLING THE HASHMAP
# nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
# def largestUniqueNumber(nums):
#     hashmap = {}
#     for num in nums:
#         hashmap[num] = hashmap.get(num, 0) + 1
#
#     ans = -1
#     for key, val in hashmap.items():
#         if val == 1:
#             ans = max(ans, key)
#     return ans
#
# print(largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]))

'''Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.'''

#from collections import defaultdict


# def maxNumberOfBalloons(text):
#     bCount = aCount = lCount = oCount = nCount = 0
#
#     for char in text:
#         if char == 'b':
#             bCount += 1
#         elif char == 'a':
#             aCount += 1
#         elif char == 'l':
#             lCount += 1
#         elif char == 'o':
#             oCount += 1
#         elif char == 'n':
#             nCount += 1
#
#     lCount //= 2
#     oCount //= 2
#
#     return min(bCount, aCount, lCount, oCount, nCount)
# text = 'nlaebolko'
# print(maxNumberOfBalloons(text))
#
# Time complexity: O(N)
# Space complexity: O(1)




# What if the text is not guaranteed to be balloon, we use this next approach, for the general case

# from collections import defaultdict
# def maxNumberOfBalloon(text):
#     def findNumberOfPattern(text, pattern):
#         answer = float('inf')
#         textfreq = defaultdict(int)
#         patternfreq = defaultdict(int)
#
#         for char in text:
#             textfreq[ord(char) - ord('a')] += 1
#
#         for char in pattern:
#             patternfreq[ord(char) - ord('a')] += 1
#
#         for i in range(26):
#             if patternfreq[i] != 0:
#                 answer = min(answer, textfreq[i] // patternfreq[i])
#         return answer
#     return findNumberOfPattern(text, 'balloon')
#
# print(maxNumberOfBalloon('leetcode'))
#
# Time Complexity: O(n+m), where n is the length of text, and m is the length of pattern
# Space: O(1),  The textfreq and patternfreq stores count for up to 26letters, which result in constant space O(1)



'''Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.'''

#BRUTE FORCE SOLUTION
# def findMaxLength(nums):
#     maxlength = 0
#     for start in range(len(nums)):
#         zeroes = 0
#         ones = 0
#         for end in range(start, len(nums)):
#             if nums[end] == 0:
#                 zeroes += 1
#             else:
#                 ones += 1
#             if ones == zeroes:
#                 maxlength = max(maxlength, end - start + 1)
#     return maxlength
# print(findMaxLength([0, 1, 0]))


#USING HASHMAP
# def findMaxLength(nums):
#     hashmap = {}
#     res = count = 0
#     for i in range(len(nums)):
#         count += 1 if nums[i] == 1 else -1
#         if count == 0:
#             res = i + 1
#         elif count in hashmap:
#             res = max(res, i - hashmap[count])
#         else:
#             hashmap[count] = i
#     return res
# print(findMaxLength([0, 1, 0]))


'''Given an array of strings strs, group the anagrams together.'''

#strs = ["eat","tea","tan","ate","nat","bat"]

# USING SORTED STRING
# from collections import defaultdict
#
# def groupAnagrams(strs):
#     hashmap = defaultdict(list)
#     for s in strs:
#         key = "".join(sorted(s))
#         hashmap[key].append(s)
#     return hashmap.keys()
#
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

#Time complexity: O(n.mlogm) where n is the number/length of string, and m is the average length of each string
# Space: O(n.m)

#USING COUNT
# from collections import defaultdict
# def groupAnagrams(strs):
#     hashmap = defaultdict(list)
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         hashmap[tuple(count)].append(s)
#
#     return hashmap.values()
#
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

'''Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.'''

# from collections import defaultdict
#
# def minimumCardPickup(cards):
#     hashmap = defaultdict(list)
#     for i in range(len(cards)):
#         hashmap[cards[i]].append(i)
#     ans = float('inf')
#     for value in hashmap.values():
#         for i in range(len(value) - 1):
#             ans = min(ans, value[i + 1] - value[i] + 1)
#
#     return ans if ans < float('inf') else -1
#
# print(minimumCardPickup([3, 4, 2, 3, 4, 7]))

# Time complexity: O(n)
# Space: O(n)

#Improved code
# from collections import defaultdict
#
# def minimumCardPickup(cards):
#     hashmap = defaultdict(int)
#     ans = float('inf')
#     for i in range(len(cards)):
#         if cards[i] in hashmap:
#             ans = min(ans, i - hashmap[cards[i]] + 1)
#         hashmap[cards[i]] = i
#     return ans if ans < float('inf') else -1
#
# print(minimumCardPickup([3, 4, 2, 3, 4, 7]))

#Sliding window solution
# cards = [3, 4, 2, 3, 4, 7]
# def minimumCardPickup(cards):
#     hashmap = {}
#     ans = float('inf')
#     left = 0
#
#     for right in range(len(cards)):
#         card = cards[right]
#
#         if card in hashmap:
#             left = max(left, hashmap[card])
#
#             ans = min(ans, right - left + 1)
#         hashmap[card] = right
#     return ans if ans != float('inf') else -1
#
# print(minimumCardPickup([3, 4, 2, 3, 4, 7, 4]))



'''Given an array of integers nums, find the maximum value of nums[i] + nums[j], where 
nums[i] and nums[j] have the same digit sum (the sum of their individual digits). Return -1 if
 there is no pair of numbers with the same digit sum.'''

# nums = [18, 43, 36, 13, 7]
# from collections import defaultdict
#
# def maximumSum(nums):
#     def get_digit_sum(num):
#         digit_sum = 0
#         while num:
#             digit_sum += num % 10
#             num //= 10
#
#         return digit_sum
#
#     dic = defaultdict(list)
#     for num in nums:
#         digit_sum = get_digit_sum(num)
#         dic[digit_sum].append(num)
#     ans = -1
#     for value in dic.values():
#         for i in range(len(value) - 1):
#             ans = max(ans, value[i] + value[i + 1])
#     return ans
#
# print(maximumSum([35,17,19,55]))
# Time complexity: O(n)
# Space complexity: O(n)

#Another solution
# nums = [18, 43, 36, 13, 7]
# from collections import defaultdict
#
# def maximumSum(nums):
#     def get_digit_sum(num):
#         digit_sum = 0
#         while num:
#             digit_sum += num % 10
#             num //= 10
#
#         return digit_sum
#
#     dic = defaultdict(int)
#     ans = -1
#     for num in nums:
#         digit_sum = get_digit_sum(num)
#         if digit_sum in dic:
#             ans = max(ans, num + dic[digit_sum])
#         dic[digit_sum] = max(num, dic[digit_sum])
#     return ans
#
# print(maximumSum([51, 71, 17, 42]))
# Time complexity: O(n)
# Space: O(n) in the worst case where every num has a different digit sum




'''Given an n x n matrix grid, return the number of pairs (R, C) where R is a row and C is a 
column, and R and C are equal if we consider them as 1D arrays'''


#BRUTE FORCE SOLUTION

# grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
# def equalPairs(grid):
#     count = 0
#     n = len(grid)
#
#
#     for r in range(n):
#         for c in range(n):
#             match = True
#
#             for i in range(n):
#                 if grid[r][i] != grid[i][c]:
#                     match = False
#                     break
#             count += int(match)
#     return count
# print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))


#HASHING SOLUTION
# grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
# from collections import defaultdict
# def equalPairs(grid):
#     def convert_to_tuple(arr):
#         return tuple(arr)
#
#     dic = defaultdict(int)
#     for row in grid:
#         dic[convert_to_tuple(row)] += 1
#
#     dic2 = defaultdict(int)
#     for col in range(len(grid[0])):
#         current_col = []
#         for row in range(len(grid)):
#             current_col.append(grid[row][col])
#
#         dic2[convert_to_tuple(current_col)] += 1
#
#     ans = 0
#     for key in dic:
#         ans += dic[key] * dic2[key]
#
#     return ans
# print(equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
# Time complexity is O(n^2)
# Space complexity is O(n^2)


'''NeetCode 3'''
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target'''

#nums = [2,7,11,15], target = 9

def TwoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Time complexity: O(n^2)
# Space complexity: O(1)

# Using Hashmap

def TwoSum(nums, target):
    n = len(nums)
    hashmap = {}


    for i in range(n):
        compliment = target - nums[i]
        if compliment in hashmap:
            return [hashmap[compliment], i]
        hashmap[nums[i]] = i
    return


# Time complexity: O(n)
# Space complexity: O(n)

'''NeetCode 4'''
'''Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.'''

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from collections import defaultdict
'''USING SORT'''
def groupAnagrams(strs):
    hashMap = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        hashMap[key].append(s)
    return list(hashMap.values())

def groupAnagrams(strs):
    hashMap = {}

    for s in strs:
        key = ''.join(sorted(s))
        if key not in hashMap:
            hashMap[key] = []

        hashMap[key].append(s)
    return hashMap.values()

#Time complexity: O(n*mlogm) where n is the number of strings, and m is the average length of each string
#Space: O(n*m) hashmap stores all n strings, each string has length <= m

'''USING COUNT'''


def groupAnagrams(strs):
    hashMap = {}
    for s in strs:
        arr = [0] * 26
        for i in s:
            arr[ord(i) - ord('a')] += 1

        key = tuple(arr)
        if key not in hashMap:
            hashMap[key] = []
        hashMap[key].append(s)
    return hashMap.values()


#Time complexity: O(n*m) The inner for loop O(m) and outer loop is O(n)
#Space complexity: O(n*m).  hashmap stores all n strings, with each average length m, Temporary count O(1) for the array
# and in worst case the tuple contains all unique keys which is O(n * 26), overall O(n*m) + O(1) + O(n * 26) = O(n*m)


'''NeetCode 7'''
'''Valid Sudoku'''

'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.'''


def isValidSudoku(board):
    N = 9
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    for r in range(len(rows)):
        for c in range(len(cols)):
            val = board[r][c]
            if board[r][c] == ".":
                continue

            if board[r][c] in rows[r]:
                return False
            rows[r].add(board[r][c])

            if board[r][c] in cols[c]:
                return False
            cols[c].add(board[r][c])

            if board[r][c] in boxes[ (r // 3) * 3 + c // 3]:
                return False
            boxes[ (r // 3) * 3 + c // 3].add(board[r][c])
    return True





import collections
def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            if (val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(val)
            rows[r].add(val)
            squares[(r // 3, c // 3)].add(val)
    return True





# print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]))

# Time: O(N^2)
# Space: O(N^2)

'''Some solid concept regarding two dimensional arrays'''
rows, cols = (5, 5)
# # 1st approach
# arr = [[0]*cols]*rows
# arr[0][0] = 1
#
# for row in arr:
#     print(row)
# when 2D arrays are created this way, changing a row will affect all the other rows

# 2nd approach
# arr = [[0 for i in range(cols)] for j in range(rows)] # Better way to declare 2D arrays
#
# arr[0][0] = 1
# for row in arr:
#     print(row)







'''You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.'''
s = 'eceba'
k = 2

def LengthOflongestkDistinctSubstring(s, k):
    hashmap = {}

    left = ans = 0

    for right in range(len(s)):
        if s[right] not in hashmap:
            hashmap[s[right]] = 0
        hashmap[s[right]] += 1

        while len(hashmap) > k:
            hashmap[s[left]] -= 1

            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


# Time: O(n)
# Space: O(k) The hashmap occupies O(k) space, as the algorithm will delete elements from the hash map once it grows beyond k




'''Neetcode 9'''
'''Longest Consecutive sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.'''

# input: nums = [100,4,200,1,3,2]
# output: 4
'''Brute force'''
def longestConsecutive(nums):
    longest = 0

    for num in nums:
        current_num = num
        current_streak = 1

        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1

        longest = max(longest, current_streak)

    return longest

# Time: O(n^3)
# Space: O(1)



'''with hashset'''
def longestConsecutive(nums):
    numSet = set(nums) # O(1) lookup time
    longest = 0

    for n in numSet:
        if n - 1 not in numSet:
            length = 0
            while ( n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

#Time: O(n)
#Space: O(n)


'LC 1814'
'Count Nice Pairs in an Array'
# nums = [42, 11, 1, 97]
def count_nice_pairs_in_array(nums):

    def rev(num):
        res = 0
        while num > 0:
            res = res * 10 + num % 10
            num //= 10
        return res
    dict = defaultdict(int)
    ans = 0
    for num in nums:
        diff = num - rev(num)
        ans += dict[diff]
        dict[diff] += 1
    return ans




