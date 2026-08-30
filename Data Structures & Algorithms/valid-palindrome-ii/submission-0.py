class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                #skipping left and going until end of string
                skipL = s[l + 1 : r + 1]
                # start from left and go to the right
                skipR = s[l : r]
                # reverse and check if it is equal to its own reversal
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1

        return True