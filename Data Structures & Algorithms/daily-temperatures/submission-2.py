class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, st, l = [0]*len(temperatures), [], 0
        while l < len(temperatures):
            while st and temperatures[st[-1]] < temperatures[l]:
                res[st[-1]] = l - st[-1]
                st.pop()
            st.append(l)
            l += 1
        return res