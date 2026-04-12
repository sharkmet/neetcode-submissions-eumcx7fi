class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', "/"]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token == '+': 
                result = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif token == '-': 
                result = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif token == '*': 
                result = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif token == '/': 
                result = math.truncate(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
        return stack[0]