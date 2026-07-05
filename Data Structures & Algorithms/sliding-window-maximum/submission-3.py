class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq, res = deque([0]), []

        for i in range(1, k):
            while dq and nums[dq[-1]] < nums[i]: dq.pop()
            dq.append(i)
        
        res.append(nums[dq[0]])

        for right in range(k, len(nums)):
            if right - k >= dq[0]: dq.popleft()

            while dq and nums[dq[-1]] < nums[right]: dq.pop()
            
            dq.append(right)
            
            res.append(nums[dq[0]])
        
        return res