class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn
        res = []
        curr = 0
        while curr < len(nums) - 2: 
            start, end , target = curr + 1, len(nums) - 1, nums[curr] * -1
            while start < end:
                act = nums[start] + nums[end]
                if act == target:
                    res.append([nums[curr], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]: start += 1
                    # while end > start and nums[end] == nums[end + 1]: end -= 1
                elif act > target: end -= 1
                else: start += 1
            
            curr += 1
            while curr < len(nums) - 1 and nums[curr] == nums[curr-1]:
                curr += 1
        return res
