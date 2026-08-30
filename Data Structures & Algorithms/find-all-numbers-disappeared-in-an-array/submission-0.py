class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        disappear = []
        for i in range(len(nums)):
            if i+1 not in nums:
                disappear.append(i+1)
        return disappear