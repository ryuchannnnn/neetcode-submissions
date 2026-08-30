class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s)-1):
            asciiVal1 = ord(s[i])
            asciiVal2 = ord(s[i+1])
            total += abs(asciiVal2 - asciiVal1)
        return total