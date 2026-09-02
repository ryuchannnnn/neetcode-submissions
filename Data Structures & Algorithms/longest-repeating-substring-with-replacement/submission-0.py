class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {
        }
        res = 0
        
        l = 0
        # sliding window
        for r in range(len(s)):
            # get count
            count[s[r]] = 1 + count.get(s[r], 0)
            # length of window - most freq char > replacements allowed
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l +=1
            # size of window
            res = max(res, r - l + 1)
        return res
            