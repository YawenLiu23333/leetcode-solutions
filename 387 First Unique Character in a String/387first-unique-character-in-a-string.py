class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for r, ch in enumerate(s):
            if count[s[r]] == 1:
                return r
        return -1
        