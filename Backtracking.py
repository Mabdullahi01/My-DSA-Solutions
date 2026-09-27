
'NeetCode 71'
'Subsets'

def subsets(nums):
    res = []

    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # Include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Not include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


# T : O( n * 2ⁿ)
# M : O(n), Auxiliary space, but if including the answer, O( n * 2ⁿ)

'NeetCode 72'
'Combination Sum'

def combinationSum(candidates, target):
    res = []

    def dfs(index, cur, total):
        if total == target:
            res.append(cur.copy())
            return

        if index >= len(candidates) or total > target:
            return

        cur.append(candidates[index])
        dfs(index, cur, total + candidates[index])

        cur.pop()
        dfs(index + 1, cur, total)

    dfs(0, [], 0)
    return res

# T: O( 2^t), where t can be the target / minimum candidate value

'NeetCode 73'
'Permutations'

def permute(nums):
    if len(nums) == 0:
        return [[]]

    # exclude the first element, [1, 2, 3]
    perms = permute(nums[1:])
    res = []
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)
    return res

# T: O(n × n!)


'Iterative Solution'

def permute(nums):
    perms = [[]]

    for n in nums:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                new_perms.append(p_copy)
        perms = new_perms

    return perms


'NeetCode 74'
'SubSet II'

def subsetWithDup(nums):
    res = []
    nums.sort()

    subset = []
    def backtrack(i):
        if i == len(nums):
            res.append(subset[::])
            return

        #include nums[i]
        subset.append(nums[i])
        backtrack(i + 1)
        subset.pop()

        #skip nums[i] and skip duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1)
    backtrack(0)

    return res

# T : O( n * 2ⁿ)


'NeetCode 75'
'CombinationSumII'

def CombinationSumII(candidates, target):
    candidates.sort()

    res = []
    def backtrack(j, curr, total):
        if total == 0:
            res.append(curr.copy())
        if total <= 0:
            return

        prev = -1
        for i in range(j, len(candidates)):
            if candidates[i] == prev:
                continue

            curr.append(candidates[i])
            backtrack(i + 1, curr, total - candidates[i])
            curr.pop()
            prev = candidates[i]

    backtrack(0, [], target)
    return res

'without using prev'
def CombinationSumII(candidates, target):
    candidates.sort()

    res = []
    def backtrack(j, curr, total):
        if total == 0:
            res.append(curr.copy())
        if total <= 0:
            return

        for i in range(j, len(candidates)):
            if i > j and candidates[i] == candidates[i - 1]:
                continue

            curr.append(candidates[i])
            backtrack(i + 1, curr, total - candidates[i])
            curr.pop()

    backtrack(0, [], target)
    return res

# T : O(2^n)


