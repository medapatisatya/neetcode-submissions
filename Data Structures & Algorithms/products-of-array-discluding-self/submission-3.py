class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr, res = 1, []
        for num in nums:
            res.append(pr*num)
            pr = pr * num
        
        i, pr = len(nums) - 1, 1
        while i >= 1:
            res[i] = pr * res[i-1]
            pr = pr * nums[i]
            i -= 1
        res[i] = pr

        return res