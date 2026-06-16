class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix sum pattern.
        pre_prod = [1]
        for num in nums[::-1]:
            pre_prod.append(pre_prod[-1] * num)
        pre_prod = pre_prod[::-1]

        pre, res = 1, []
        for i in range(len(nums)):
            res.append(pre * pre_prod[i+1])
            pre = pre * nums[i]
        
        return res