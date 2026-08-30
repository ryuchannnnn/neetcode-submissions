class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) time and space
        if(len(s) != len(t)):
            return False
        countS, countT = {}, {} # creating hashmap
        for i in range(len(s)):
            # count occurence of each character
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            # check each count
            if countS[c] != countT.get(c,0):
                return False
        return True

        # 1 liner same as above
        # return Counter(s) == Counter(t)

        # brute force // n log n
        # sortedStr = ''.join(sorted(s))
        # sortedStr2 = ''.join(sorted(t))
        # if(sortedStr == sortedStr2):
        #     return True
        # return False