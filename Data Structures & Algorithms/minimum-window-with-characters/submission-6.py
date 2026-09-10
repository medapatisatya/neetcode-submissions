class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        l, ct, cw, ml, ra = 0, {}, {}, float("infinity"), [-1,-1]

        for c in t: ct[c] = ct.get(c, 0) + 1
        required = len(ct)
        have = 0

        for r in range(len(s)):
            c = s[r]

            cw[c] = cw.get(c, 0) + 1
            if c in ct and cw[c] == ct[c]: have += 1
            
            while have == required:
                if r - l + 1 < ml:
                    ml, ra = r - l + 1, [l, r]
                
                cw[s[l]] -= 1
                if s[l] in ct and cw[s[l]] < ct[s[l]]:
                    have -= 1
                
                l += 1
        
        return s[ra[0]:ra[1]+1] if ml != float("infinity") else ""
