class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l+h)//2
            if nums[m] < nums[h]:
                h = m
            else:
                l = m + 1
        
        return l
    

    def bin_search(self, nums: List[int], target: int, l:int, h:int):
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        return -1


    def search(self, nums: List[int], target: int) -> int:
        start = self.findMin(nums)
        
        if nums[start] <= target <= nums[-1]:
            right = self.bin_search(nums, target, start, len(nums) - 1)
            if right != -1: return right
        else:
            left = self.bin_search(nums, target, 0, start - 1)
            if left != -1: return left
        
        return -1
