
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        n = len(heights)
        
        #interate through the amount of buildings
        for i in range(n-1):
            diff = heights[i+1] - heights[i] # calculate diff in height
            
            if diff > 0:
                heapq.heappush(q, diff) #continue 
            
            if len(q) > ladders:
                bricks = bricks - heapq.heappop(q)
            
            if bricks < 0:
                return i
        return n - 1