class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store prev elements
        hashmap = {

        }
        for i in range(len(nums)):
            # check if difference is alr in hashmap
            difference = target - nums[i]
            if difference in hashmap:
                # return solution
                return [hashmap[difference], i]
            # update hashmap  
            hashmap[nums[i]] = i
        # brute force
        # for i in range(len(nums)):
        #     differ = target - nums[i]
        #     j = i + 1
        #     for j in range(len(nums)):
        #         if(differ == nums[j]):
        #             return [i,j]        