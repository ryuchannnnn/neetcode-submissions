class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force 
        prefix = 1
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix = nums[i] * prefix
        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] = output[j] * postfix
            postfix = nums[j] * postfix
        return output