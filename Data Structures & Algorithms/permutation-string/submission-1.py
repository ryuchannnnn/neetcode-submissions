class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False
        
        # convert char to int and using them as indexes
        s1Count, s2Count = [0] * 26, [0] * 26
        # go through every charcter in s1 and s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] +=1
            s2Count[ord(s2[i]) - ord('a')] +=1
        
        matches = 0
        # add 1 if the index is the same, so if they both have a then add 1
        for i in range(26):
            matches+= (1 if s1Count[i] == s2Count[i] else 0)

        # sliding window part
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True
            # update matches on the right side
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            #char was just added into window, so you need to check matches
            if s1Count[index] == s2Count[index]:
                matches+=1
            # possible that by increment, it could've been too large
            elif s1Count[index] + 1 == s2Count[index]:
                matches-=1
            # subtracting a character on the left side bc you removed a char
            index = ord(s2[l]) - ord('a')
            # decrement count
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches+=1
            elif s1Count[index] - 1 == s2Count[index]:
                matches-=1
            l+=1
        return matches == 26
        