class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # keep track of values in window 
        window = set()
        l = 0
        for R in range(len(nums)):
            # window is too big
            if R - l > k:
                window.remove(nums[l])
                l += 1
            # if value is already in window
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
        