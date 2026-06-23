class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0,len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            l,r = i+1, len(nums)-1
            while l<r:
                current_sum, target = nums[l] + nums[r], 0 - nums[i]
                if current_sum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]: l += 1
                elif target > current_sum: l += 1
                else: r -= 1
        return res