class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, maxa = [], 0

        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                index, height = st.pop()
                maxa = max(maxa, (i - index) * height)
                start = index
            st.append((start, h))
        
        for i, h in st:
            maxa = max(maxa, (len(heights)-i)*h)
        
        return maxa