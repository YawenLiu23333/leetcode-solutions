class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        stack = []
        l, r = 0, len(nums) -1
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                stack.append(nums[l]* nums[l])
                l += 1
            else:
                stack.append(nums[r]* nums[r])
                r -= 1
        return stack[::-1]

