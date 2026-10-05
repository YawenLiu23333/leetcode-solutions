class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        valid = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in valid:
                valid.remove(s[l])
                l += 1
            valid.add(s[r])
            res = max(r - l + 1, res)
        return res