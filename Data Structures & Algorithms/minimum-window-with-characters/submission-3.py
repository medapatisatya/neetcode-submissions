class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        tmap, smap = {}, {}
        left, matches = 0, 0

        min_range, min_len = [0, len(s)], len(s) + 1
        for ch in t: tmap[ch] = tmap.get(ch, 0) + 1

        for right in range(len(s)):
            ch = s[right]
            smap[ch] = smap.get(ch, 0) + 1

            if ch in tmap and smap[ch] == tmap[ch]: matches += 1
            
            while matches == len(tmap):
                if (right - left + 1) < min_len:
                    min_range = [left, right]
                    min_len = right - left + 1
                
                smap[s[left]] -= 1

                if s[left] in tmap and smap[s[left]] < tmap[s[left]]:
                    matches -= 1
                
                left += 1
        
        return s[min_range[0]:min_range[1]+1] if min_len != len(s) + 1 else ""

