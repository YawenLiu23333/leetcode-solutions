class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        l = len(nums) * 2
        stack = []
        for i in range(l):
            if i < len(nums):
                while stack and nums[i] > stack[-1][0]:
                    n, ind = stack.pop()
                    ans[ind] = nums[i]
                stack.append((nums[i], i))
            else:
                i %= len(nums)
                while stack and nums[i] > stack[-1][0]:
                    n, ind = stack.pop()
                    ans[ind] = nums[i]
        return ans



