class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                num = stack.pop()
                res[num] = n
            stack.append(n)
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            ans[i] = res.get(nums1[i], -1)
        return ans



