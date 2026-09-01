class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()
        for ind, num in enumerate(nums):
            if num in diff:
                return [diff[num], ind]
            diff[target-num] = ind
        