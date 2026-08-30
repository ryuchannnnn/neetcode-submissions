class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0,0
        # while both ptrs are inbound
        while i < len(word) and j < len(abbr):
            # increment if theyre both the same
            if word[i] == abbr[j]:
                i,j = i + 1, j + 1
            # this executes if j is diff than i or its 0
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            # since neither executes, it means abbr[j] is a number
            else:
                sublen = 0
                while j < len(abbr) and not abbr[j].isalpha():
                    # initial 0 so it wont do anything but if sublen > 0 
                    # then itll turn it into double digit
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                # shift i ptr by amount of sublen
                i += sublen
        # when l ptr is out of bounds and j as well
        return i == len(word) and j == len(abbr)

