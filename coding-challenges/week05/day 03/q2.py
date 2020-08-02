class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        if len(nums) == 2: return nums.index(max(nums))
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r -l ) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l