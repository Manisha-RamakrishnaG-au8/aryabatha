class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n  = len(nums)
        ans = [-1]*n
        for i,ele in enumerate(nums*2):
            i%=n
            if not stack:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < ele:
                    pos = stack.pop()
                    ans[pos] = ele
                stack.append(i)
        return ans