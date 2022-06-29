class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum, rightSum = 0, 0 #prefix and postfix sums
        
        for i in range(len(nums)):
            
            rightSum = totalSum - leftSum - nums[i] # subtract the pivot index
            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]
            
        return -1