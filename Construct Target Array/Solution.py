class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # 1,1 -> 1,2 -> 3,2 -> 3,5 -> 8,5
        # 1*n will always be first digit 
        
        heap = [-num for num in target]
        total = sum(target)
        heapify(heap)
        
        while heap[0] != -1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1 : return False
            num %= total
            total += num
            heappush(heap, -num or -total)
        
        return True