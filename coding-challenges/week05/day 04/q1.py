class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        
        for i in range(len(nums)):
            second = target - nums[i]
            if second in nums_dict:
                return [nums_dict[second], i]
            nums_dict[nums[i]] = i
