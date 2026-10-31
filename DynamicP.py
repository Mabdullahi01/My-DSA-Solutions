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

'NC 99'
'Climbing Stairs'
'Bottom up'
def climbstairs(n):

    if n == 1:
        return 1
    dp = [ 0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

'Top down'
def climbStairs(n):
    memo = {}

    def dp(i):
        if i == 1:
            return 1

        if i == 2:
            return 2

        if i in memo:
            return memo[i]

        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)

'Bottom up with array'
def Climbstair(n):
     dp = [0] * ( n + 1)

     dp[0] = 1 #taking no of ways to climb zero stairs as 1, meaning take no steps
     dp[1] = 1

     for i in range(2, n + 1):
         dp[i] = dp[i - 1] + dp[i - 2]
     return dp[n]
#T : O(n)
# M: O(n)


'Bottom Up with Optimized space'
def climbStair(n):
    one, two = 1, 0

    for i in range(n):
        tmp = one
        one = one + two
        two = tmp

    return one

#T : O(n)
# M: O(1)
























