class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m, s2m, matches, left = [0] * 26, [0] * 26, 0, 0

        if len(s1) > len(s2): return False

        for i in range(len(s1)):
            s1m[ord(s1[i]) - 97] += 1
            s2m[ord(s2[i]) - 97] += 1
        
        for i in range(26):
            if s1m[i] == s2m[i]: matches += 1
        
        for right in range(len(s1), len(s2)):
            if matches == 26: return True
            
            chv = ord(s2[right]) - 97
            s2m[chv] += 1
            if s2m[chv] == s1m[chv]: matches += 1
            elif s2m[chv] - 1 == s1m[chv]: matches -= 1

            chv = ord(s2[left]) - 97
            s2m[chv] -= 1
            if s2m[chv] == s1m[chv]: matches += 1
            elif s2m[chv] + 1 == s1m[chv]: matches -= 1
            

            left += 1

        return matches == 26