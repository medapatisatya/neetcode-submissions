class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m, l, r, ml = dict(), 0, 0, 0
        while r < len(s):
            ch = s[r]
            if ch in m and l <= m[ch]:
                ml = max(ml, r - l)
                l = m[ch] + 1
            m[ch] = r
            r += 1
        return max(ml, r - l)