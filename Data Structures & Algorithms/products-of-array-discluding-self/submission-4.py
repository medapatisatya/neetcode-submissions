class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr, res = 1, []
        for num in nums:
            res.append(pr)
            pr = pr * num
        
        i, pr = len(nums) - 1, 1
        while i >= 0:
            res[i] = pr * res[i]
            pr = pr * nums[i]
            i -= 1

        return res