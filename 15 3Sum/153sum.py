class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #uses 2 nested loops (one for first number, pointers for 2 other numbers)
        res = []
        nums.sort()
        
        for i in range(len(nums) - 1):
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
            
        return res
        
  

    
    
    
    
 
            
    

            
    
    
    
    
    