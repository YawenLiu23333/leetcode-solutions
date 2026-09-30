class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # did this porblem months ago and i thought of this implementation before i realized i learned the exact way before, then had to derive implemntation details by myself
        if len(s2) < len(s1):
            return False
        #contains means s2 has at least qual length as s1
        count, cur = {}, {}
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
            cur[s2[i]] = 1 + cur.get(s2[i], 0)
            #changed default dict to dict to avoid compareing problems in window

        if count == cur:
            return True # does order here matter in hashmap? how deos it get evaluated 

        #check if each window contains a valid permutation
        l = 0
        for r in range(len(s1), len(s2)):
            cur[s2[r]] = 1+ cur.get(s2[r], 0)
            cur[s2[l]] -= 1
            if cur[s2[l]] == 0:
                del cur[s2[l]]
            l += 1
           
            print('cur:', cur, 'count:', count)
            if cur == count:
                return True

        return False




        