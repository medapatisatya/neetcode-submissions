class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort and compare.
        # s_map = dict()
        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     if sorted_s in s_map: s_map[sorted_s].append(s)
        #     else: s_map[sorted_s] = [s]
        
        # return list(s_map.values())

        # Using Hashmaps
        s_map = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            s_map[tuple(counter)].append(s)
        
        return list(s_map.values())
