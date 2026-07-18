class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid > 0 and nums[mid-1] > nums[mid]: return nums[mid]
            elif nums[mid] < nums[-1]: high = mid - 1
            else: low = mid + 1
        
        return nums[0]