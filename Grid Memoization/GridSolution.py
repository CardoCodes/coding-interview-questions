class Solution:
    def gridTraveler(m, n):
        if( m == 1 & n ==1):
            return 1
        if(m == 0 & n == 0):
            return 1
        return Solution.gridTraveler(m - 1, n) + Solution.gridTraveler(m, n -1);
