class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        # sliding window in l and r
        l = 0
        res = 0
        for r in range(len(s)):
            # if character at right ptr is in character set, update window      
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res,r - l + 1)
        return res