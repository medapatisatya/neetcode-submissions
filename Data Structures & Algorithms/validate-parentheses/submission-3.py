class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {')':'(', '}':'{', ']':'['}
        st = []

        for p in s:
            if p in pmap:
                if not st or (st and not st[-1] == pmap[p]): return False
                else: st.pop()
            else:
                st.append(p)
        return not st