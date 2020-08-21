class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        if len(nums)<=2:
            return max(nums)
        total=[0 for i in range(len(nums))]
        total[0]=nums[0]
        total[1]=nums[1]
        for i in range(2,len(nums)):
            total[i]=max(total[:i-1])+nums[i]
        return max(total)