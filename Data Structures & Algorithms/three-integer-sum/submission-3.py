class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the array
        nums.sort()

        for i, a in enumerate(nums):
            # not the first value and a is the same as preValue
            if i > 0 and a == nums[i-1]:
                continue
            # 2ptr soln
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    # if numbers are the same and l < r still
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
        return res
