class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch not in m: st.append(ch)
            else:
                if not st: return False
                else:
                    p = st.pop()
                    if not p == m[ch]: return False

        if not st: return True
        return False