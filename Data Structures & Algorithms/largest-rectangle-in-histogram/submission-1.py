class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, prev, ma = [], -1, 0

        for ind, h in enumerate(heights):
            while st and heights[st[-1][1]] > h:
                ma = max(ma, (ind-st[-1][0]-1)*heights[st[-1][1]])
                prev = st[-1][0]
                st.pop()
            if st: st.append([st[-1][1], ind])
            else: st.append([prev, ind])
        
        for item in st:
            ma = max(ma, (len(heights)- item[0]-1)*heights[item[1]])
        
        return ma