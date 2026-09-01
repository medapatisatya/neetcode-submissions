class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = dict()
        for s in strs:
            chs = [0] * 26
            for i in s:
                chs[ord(i) - ord('a')] += 1
            tchs = tuple(chs)
            if tchs in mapper:
                mapper[tchs].append(s)
            else:
                mapper[tchs] = [s]
        
        return list(mapper.values())