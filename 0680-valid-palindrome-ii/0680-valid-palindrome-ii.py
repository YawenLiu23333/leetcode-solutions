class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                left = s[l+ 1: r +1]
                right = s[l: r]
                return left[::-1] == left or right[::-1] == right
        return True