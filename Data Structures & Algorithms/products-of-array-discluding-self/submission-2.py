class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix sum pattern.
        # pre_prod is getting calculating from back.
        # pre_prod = [1]
        # for num in nums[::-1]:
        #     pre_prod.append(pre_prod[-1] * num)
        # pre_prod = pre_prod[::-1]

        # pre, res = 1, []
        # for i in range(len(nums)):
        #     res.append(pre * pre_prod[i+1])
        #     pre = pre * nums[i]
        # return res

        # pre_prod is getting calculating from front.
        # pre_prod = [1]
        # for num in nums:
        #     pre_prod.append(pre_prod[-1]*num)
        # pre, res = 1, [0 for i in range(len(nums))]
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] = pre * pre_prod[i]
        #     pre = pre * nums[i]
        # return res

        # Using output array as storage.
        # without using any additional storage.
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        
        return res




