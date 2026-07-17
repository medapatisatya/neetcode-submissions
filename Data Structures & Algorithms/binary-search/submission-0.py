class Solution:
    def search_recursive(self, nums: List(int), target: int, i: int, j:int):
        if i > j: return -1
        m = (i+j) // 2
        if nums[m] == target: return m
        elif nums[m] < target: return self.search_recursive(nums, target, m+1, j)
        else: return self.search_recursive(nums, target, i, m-1)

    def search(self, nums: List[int], target: int) -> int:
        # Recursive
        #return self.search_recursive(nums, target, 0, len(nums)-1)

        #Iterative
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == target: return m
            elif nums[m] < target: i = m + 1
            else: j = m - 1
        return -1