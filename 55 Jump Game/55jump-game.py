class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        res = True
        cur = 0
        
        for i in range(len(nums) -2, -1, -1):
      

            if nums[i] == 0:
                res = False
                
            if not res:
                if nums[i] > cur:
                    cur = 0
                    res = True
                else:
                    cur += 1
            
                
        return res
        
            