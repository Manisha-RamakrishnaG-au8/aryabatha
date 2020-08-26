class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        ls = [nums[0]]
        for num in range(1,len(nums)):
            if nums[num] > ls[-1]: ls.append(nums[num])
            else:
                start, end = 0, len(ls)-1
                while start < end:
                    mid = (start+end)//2  
                    if ls[mid] == nums[num]:
                        start = mid
                        break
                    elif ls[mid] > nums[num]: end = mid
                    else: start = mid+1
                ls[start] = nums[num]
            
        return len(ls)
        