class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        mid = sorted(nums) [n//2]
        
        solution = sum(abs(i-mid) for i in nums)
        return solution