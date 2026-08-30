class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 == 1:
            return False
        hashmap = {
            # key : value
            ")" : "(",
            "}" : "{",
            "]"  : "["
        }
        stack = []
        for i in range(len(s)):
            if s[i] in hashmap.keys(): # check for valid closing parenthesis
                if(stack and stack[-1] == hashmap[s[i]]):
                    stack.pop()
                else:
                    return False
            else: # this is an open parenthesis
                stack.append(s[i])
        if(len(stack) == 0):
            return True
        else:
            return False