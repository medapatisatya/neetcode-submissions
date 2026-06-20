class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums_hash = set(nums)
        i, count = 0, 0
        while i < len(nums):
            if not nums[i] - 1 in nums_hash:
                max_count, x = 1, nums[i]
                while x+1 in nums_hash:
                    max_count += 1
                    x += 1
                count = max(max_count, count)
            i += 1
        return count
                