class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)< len(p):
            return []
        res = []
        pcount = [0]*26
        scount = [0]*26
        for i in range(len(p)):
            pcount[ord(p[i])- ord('a')] += 1
            scount[ord(s[i])- ord('a')] += 1
        if pcount == scount:
            res.append(0)

        for i in range(len(p), len(s)):
            scount[ord(s[i])- ord('a')] += 1
            scount[ord(s[i - len(p)]) - ord('a')] -= 1
            if scount == pcount:
                res.append(i - len(p) + 1)
        return res

        