class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, res, i = [], [0]*len(temperatures), len(temperatures) - 1

        while i >= 0:
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            
            if not st:
                res[i] = 0
            else:
                res[i] = st[-1] - i
            
            st.append(i)
            i -= 1
        return res