class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowls = ['a','e', 'i','o','u']
        l, r = 0, len(s) - 1
        while l < r:
            if s[l].lower() not in vowls:
                l += 1
            elif s[r].lower() not in vowls:
                r -= 1
            else:
                s[l], s[r] = s[r],s[l]
                l += 1
                r -= 1
        res = ''.join(s)
        return res
            
        