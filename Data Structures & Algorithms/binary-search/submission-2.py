class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Iterative
        # l,h = 0, len(nums) - 1
        # while l <= h:
        #     mid = (l+h) // 2
        #     if nums[mid] == target: return mid
        #     elif nums[mid] < target: l = mid + 1
        #     else: h = mid - 1
        # return -1

        # Recursion
        def rsearch(nums, l, h, target):
            if l > h: return -1

            mid = (l+h) // 2
            if nums[mid] == target: return mid
            if nums[mid] < target: return rsearch(nums, mid+1, h, target)
            return rsearch(nums, l, mid-1, target)
        
        return rsearch(nums, 0, len(nums)-1, target)