class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {target-nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in tracker: return [tracker[nums[i]], i]
            tracker[target - nums[i]] = i