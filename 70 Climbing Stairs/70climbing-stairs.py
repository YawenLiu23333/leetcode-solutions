class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        temp = None
        
        while n - 1 > 0:
            temp = one + two
            two = one
            one = temp
            
            n  -= 1
            
        return one