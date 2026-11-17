class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = set()
        for n in set1:
            if n in set2:
                res.add(n)

        return list(res)
