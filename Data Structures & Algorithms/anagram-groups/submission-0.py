class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort and compare.
        s_map = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in s_map: s_map[sorted_s].append(s)
            else: s_map[sorted_s] = [s]
        
        return list(s_map.values())
