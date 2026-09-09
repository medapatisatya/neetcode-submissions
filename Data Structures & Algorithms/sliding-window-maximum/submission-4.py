class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, st, res = 0, [], []
        for r in range(0, len(nums)):
            while st and nums[st[-1]] < nums[r]: st.pop()
            st.append(r)

            if r - l + 1 == k:
                res.append(nums[st[0]])
                l += 1
                if st[0] < l: st.pop(0)
        return res