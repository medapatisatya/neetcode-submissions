class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {')':'(', '}':'{', ']':'['}
        st = []

        # for p in s:
        #     if p in pmap:
        #         if not st or (st and not st[-1] == pmap[p]): return False
        #         else: st.pop()
        #     else:
        #         st.append(p)
        # return not st
        for p in s:
            if not p in pmap: st.append(p)
            else:
                if not st: return False
                elif st.pop() != pmap[p]: return False
        return not st