class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) -1
        while l < r:
            soom = numbers[l] + numbers[r]
            if soom > target:
                r -= 1
            elif soom < target:
                l += 1
            else:
                return [l + 1, r + 1]
            
            
            
        