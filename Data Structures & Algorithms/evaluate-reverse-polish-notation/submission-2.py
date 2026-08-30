class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in range(len(tokens)):
            if(tokens[item] == "+"):
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 + num2
                stack.append(total)
            elif(tokens[item] == "-"):
                num1 = stack.pop()
                num2 = stack.pop()
                total = num2 - num1
                stack.append(total)
            elif(tokens[item] == "*"):
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 * num2
                stack.append(total)
            elif(tokens[item] == "/"):
                num1 = stack.pop()
                num2 = stack.pop()
                total = int(float(num2) / num1)
                stack.append(total)
            else:
                stack.append(int(tokens[item]))
        finalTotal = stack.pop()
        return finalTotal