class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # 1,1 -> 1,2 -> 3,2 -> 3,5 -> 8,5
        # 1*n will always be first digit 
        
        heap = [-num for num in target] #create heap from target list
        total = sum(target) #total total is sum of target 
        heapify(heap)
        
        while heap[0] != -1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1 : return False # false if -heappop(num) is less than or equal to total 
            
            num %= total
            total += num
            heappush(heap, -num or -total)
        
        return True