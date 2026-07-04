class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch not in m: st.append(ch)
            elif not st or st.pop() != m[ch]: return False

        return len(st) == 0