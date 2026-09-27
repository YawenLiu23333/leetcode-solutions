class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = float('-inf')
        while l < r:
            cur = (r - l) * min(height[l], height[r])
            res = max(res, cur)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res

