class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wl, wr, ml, m = 0, 0, 0, dict()
        for i, ch in enumerate(s):
            if ch in m:
                ml = max(ml, wr - wl)
                wl = max(wl, m[ch] + 1)
            m[ch] = i
            wr += 1
        return max(ml, wr - wl)