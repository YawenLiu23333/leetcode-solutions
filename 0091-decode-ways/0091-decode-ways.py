class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def dfs(i):
        # Base case: successfully decoded everything
            if i == len(s):
                return 1

        # Base case: invalid leading zero
            if s[i] == "0":
                return 0

        # Explore taking one digit
            take1 = dfs(i + 1)

        # Explore taking two digits, only if valid
            take2 = 0
            if i < len(s) - 1 and 10 <= int(s[i: i + 2]) <= 26: 
                take2 = dfs(i + 2)

        # Return total number of valid decodings
            return take1 + take2

        return dfs(0)