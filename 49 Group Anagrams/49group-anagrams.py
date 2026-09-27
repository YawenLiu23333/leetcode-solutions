class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = defaultdict(list)
        for s in strs:
            check = [0]*26
            for c in s:
                check[ord(c)-ord('a')] += 1
            group[tuple(check)].append(s)

        return [ans for ans in group.values()]
            
        