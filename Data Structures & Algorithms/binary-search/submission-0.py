class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # a basic binary search
        l = 0
        # array length - 1
        r = len(nums) - 1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        