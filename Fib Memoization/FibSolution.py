



class Solution:
    #Using memoization we can store the values we have already computed, we store this in a hashmap using key value pair
    def fibMemo(n, memo = {}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = (Solution.fibMemo(n - 1, memo) + Solution.fibMemo(n-2, memo))
        return memo[n]

    #Bad implementation, might work for small n size but given a large n time complexity is too large
    def fib(n):
        if n <= 2:
            return 1
        return Solution.fib(n-1) + Solution.fib(n-2)

print(Solution.fibMemo(10))