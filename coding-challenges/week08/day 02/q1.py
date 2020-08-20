class Solution(object):
     def twoSum(self, nums, target):


    seen ={}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in seen:
            return [seen[x],i]
        seen[nums[i]] = i
    return False
