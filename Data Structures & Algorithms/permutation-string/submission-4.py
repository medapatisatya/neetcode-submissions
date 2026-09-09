class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1l, s2l = [0] * 26, [0] * 26

        for ch in s1:
            s1l[ord(ch) - ord('a')] += 1
        
        for ch in s2[:len(s1)]:
            s2l[ord(ch) - ord('a')] += 1
        
        l = 0
        for ch in s2[len(s1):]:
            if s1l == s2l: return True
            s2l[ord(s2[l]) - ord('a')] -= 1
            s2l[ord(ch) - ord('a')] += 1
            l += 1
        return s1l == s2l