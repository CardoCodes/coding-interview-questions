class Solution:
    def climbStairs(self, n: int) -> int:
        def dphelper(n, memo):
            if n == 0 or n == 1:
                return 1
            elif n < 0:
                return 0
            elif n in memo:
                return memo[n]
            else:
                memo[n] = dphelper(n-2, memo) + dphelper(n-1, memo)
                return memo[n]
        return dphelper(n, {})
            