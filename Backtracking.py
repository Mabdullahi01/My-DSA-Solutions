
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



