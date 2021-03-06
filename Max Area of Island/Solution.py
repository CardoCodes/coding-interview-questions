class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        """
        
        """
        
        row, col = len(grid), len(grid[0]) # max values possible(prevent index out of bounds)
    
        def dfs(i, j):
            if 0 <= i <= row - 1 and 0 <= j <= col -1 and grid[i][j]:
                #set postion equal to 0 so that we know we already visited
                grid[i][j] = 0
                
                # recursive dfs for each block vertical or horizontal
                return 1 + dfs(i-1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j+ 1)
            return 0
        
        return max(dfs(i,j) for i in range(row) for j in range(col))
            
        
                