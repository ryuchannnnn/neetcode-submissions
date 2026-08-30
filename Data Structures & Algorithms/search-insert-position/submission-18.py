class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # find it then return 
            if target == nums[mid]:
                return mid
            # start binary search if you dont find it
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        # remember that if you dont find it, then 
        # L and R would be together and Left should  never be right of right (if target is smaller) and if target is bigger, then it would start the search and left would move 
        return l