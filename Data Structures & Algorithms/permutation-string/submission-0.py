class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m, s2m = [0]*26, [0]*26
        left = 0
        
        for ch in s1:
            s1m[ord(ch)-97] += 1
        
        for right in range(len(s2)):

            s2m[ord(s2[right])-97] += 1
            
            while (right-left+1) > len(s1):
                s2m[ord(s2[left])-97] -= 1
                left += 1
            
            if (right-left+1) == len(s1) and s1m == s2m: return True
        
        return False