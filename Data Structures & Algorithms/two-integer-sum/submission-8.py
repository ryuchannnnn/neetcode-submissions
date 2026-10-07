class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hm = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if diff == nums[j]:
        #             return [i,j]
        #         else:
        #             hm[i] = nums[j]
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i