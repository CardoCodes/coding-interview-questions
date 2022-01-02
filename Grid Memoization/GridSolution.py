class Solution:
    def gridTraveler(m, n, memo = {}):
        key = m + ',' + n
        if key in memo:
            return memo[key]
        if( m == 1 & n ==1):
            return 1
        if(m == 0 & n == 0):
            return 1
        
        memo[key] = Solution.gridTraveler(m - 1, n) + Solution.gridTraveler(m, n-1)
        return memo[key]
