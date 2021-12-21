

class Solution:
    def twoSum(nums, target):
        #initialize a hash map to store values
        lookup = {}

        #loop through the length of nums
        for i in range(0, len(nums)):

            #Check to see if the current nums[i] is a second value to another nums[?] that makes a pair that is equal to target
            if nums[i] in lookup.keys():
                return [lookup[nums[i]], i]

            #Use the current nums[i] and constant target to determine the second value needed i.e (9-2 = 7)
            lookup[target - nums[i]] = i

        #Here to make sure we are returning something    
        return(0, len(nums)-1)

print(Solution.twoSum(  nums = [4, 9, 2, 7, 11, 15], target = 9))
