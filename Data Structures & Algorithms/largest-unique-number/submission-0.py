class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                seen.remove(nums[i])
                continue
            else:
                seen.add(nums[i])
        if len(seen) == 0:
            return -1
        else:
            unique = max(seen)
        return unique