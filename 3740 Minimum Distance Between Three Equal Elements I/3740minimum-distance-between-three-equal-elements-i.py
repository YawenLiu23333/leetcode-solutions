class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return - 1
        good = defaultdict(list)
        for i, n in enumerate(nums):
            good[n].append(i)
        
        res = float('inf')
        
        for idxs in good.values():
            if len(idxs) >= 3:
                # print('good exists', len(idxs))
                for i in range(len(idxs) - 2):
                    res = min(res, 2* (idxs[i+2] - idxs[i]))
                    # print(res)
        return res if res!= float('inf') else - 1
