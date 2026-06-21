class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointer approach
        # front, rear = 0, len(s) - 1
        # while front < rear:
        #     while (not s[front].isalnum()) and front < rear:
        #         front += 1
        #     while (not s[rear].isalnum()) and front < rear:
        #         rear -= 1
        #     if not s[front].lower() == s[rear].lower(): return False
        #     front += 1
        #     rear -= 1
        # return True

        # One liner
        return (t := "".join([x.lower() for x in s if x.isalnum()])) == t[::-1]