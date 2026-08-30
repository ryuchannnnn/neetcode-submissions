class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = 1 + dict.get(nums[i],0)
        return max(dict, key=dict.get)
