class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while start < len(s) and not s[start].isalnum():
                start += 1

            while end > -1 and not s[end].isalnum():
                end -= 1
            
            if start < end and not s[start].lower() == s[end].lower():
                return False
            start += 1
            end -= 1
        return True