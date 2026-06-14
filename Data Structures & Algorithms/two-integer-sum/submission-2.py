class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = dict()
        for i in range(0, len(nums)):
            if nums[i] in tracker: return [tracker[nums[i]], i]
            tracker[target - nums[i]] = i