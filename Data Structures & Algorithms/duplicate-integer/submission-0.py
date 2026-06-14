class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash set approach
        unique = set()
        for num in nums:
            if num in unique: return True
            unique.add(num)
        return False

        # sorting approach
        # Bubble sort.
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]: return True
        #         elif nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        # return False
