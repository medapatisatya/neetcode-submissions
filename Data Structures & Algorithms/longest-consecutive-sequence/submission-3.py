class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        highest, count =  0, 1

        for ind, num in enumerate(nums):
            if num - 1 in s: continue
            while num + count in s:
                count += 1
            highest = max(highest, count)
            count = 1
        return highest
