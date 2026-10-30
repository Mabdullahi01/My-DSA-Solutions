'DP'

'Fibonacci with Memoization'
'Top down'
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

memo = {}

'Bottom Up Approach'

def fibonacci(n):
    arr = [0] * (n + 1)
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]

'LC 746'
'Minimum cost climbing stairs'
'Top down'
def minCostClimbingStairs(cost):

    def dp(i):
        if i <= 1:
            return 0

        if i in memo:
            return memo[i]

        memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
        return memo[i]
    memo = {}
    return dp(len(cost))

'Bottom Up'

def minCostClimbingStair(cost):
    n = len(cost)

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min( dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]

