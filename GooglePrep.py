from collections import defaultdict

def groupAnagrams(strs):
    hashmap = defaultdict(list)
    for i in strs:
        arr = [0] * 26

        for c in i:
            arr[ord(c) - ord('a')] += 1

        hashmap[tuple(arr)].append(i)

    return hashmap.values()




'Valid Anagram 242'


def isAnagram(self, s: str, t: str) -> bool:
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    for c in s:
        dict1[c] += 1

    for c in t:
        dict2[c] += 1

    return dict1 == dict2

def isanagram(s, t):
    if len(s) != len(t):
        return False

    arr = [0] * 26
    for c in s:
        arr[ord(c) - ord('a')] += 1
    for c in t:
        arr[ord(c) - ord('a')] -= 1
        if arr[ord(c) - ord('a')] < 0:
            return False
    return True

'Longest Common Prefix LC 14'

def LongestCommonPrefix(strs):
    'flower' 'flow' 'flight'
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res


def longestCommonPrefix(strs):

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]


'Zigzag Conversion LC 6'

def convert(s, numRows):
    if numRows == 1:
        return s

    res = ""
    for r in range(numRows):
        increment = 2 * (numRows - 1)
        for i in range(r, len(s), increment):
            res += s[i]
            if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                res += s[i + increment - 2 * r]
    return res

'Palindrome Number LC 9'

def palindromeNum(x):
    if x < 0: return False

    div = 1
    while x > 10 * div:
        div *= 10

    while x:
        right = x % 10
        left = x // div

        if left != right:
            return False
        x = x % div
        x = x // 10
        div = div // 100
    return True

print(palindromeNum(101))







