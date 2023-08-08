class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                res = a + stack[-1]
                if res > 0:
                    a = 0
                elif res < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
                    
            if a:
                stack.append(a)
                
        return stack
                
                
        

        
            
        