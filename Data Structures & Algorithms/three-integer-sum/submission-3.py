class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,n in enumerate(nums[:-2]):
            if n > 0: break
            
            if i > 0 and nums[i] == nums[i-1]: continue

            j,k = i + 1, len(nums) - 1
            while j < k:
                target = 0 - n
                s = nums[j] + nums[k]
                if target == s:
                    res.append([n, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < len(nums) and nums[j] == nums[j-1]:
                        j += 1
                elif target < s: k -= 1
                else: j += 1
        return res