class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # calls a hashset
        seen = set()
        # go through every input value
        for num in nums:
            # see if it exists in our hashset already
            if num in seen:
                return True
            seen.add(num)
        return False