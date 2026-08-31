class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using set
        s = set()
        for num in nums:
            if num in s: return True
            s.add(num)
        return False

        # Using sorting O(nlogn)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]: return True
        # return False