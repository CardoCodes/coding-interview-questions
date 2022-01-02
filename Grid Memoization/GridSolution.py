class Solution:
    #add memoization with hashmap
    def gridTraveler(m, n, memo = {}):
        #make a key that combines current m & n values
        key = m + ',' + n
        #search for key in memo and if it exists then return the resulting value, this makes it so that you dont repreat already calculated m & n 
        if key in memo:
            return memo[key]
        
        #base cases for return 1 possible path
        if( m == 1 & n ==1):
            return 1
        if(m == 0 & n == 0):
            return 1
        
        #create memo with new grid travel dimensions, similiar to fib
        memo[key] = Solution.gridTraveler(m - 1, n) + Solution.gridTraveler(m, n-1)
        return memo[key]
