import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda a, b: int(a/b)}
        current_result = 0
        if not tokens:
            return 0
        for i in range(len(tokens)):
            if tokens[i] in operators.keys():
                num1 = stack.pop()
                num2 = stack.pop()
                current_result = operators[tokens[i]](num2, num1)
                stack.append(current_result)
            else:
                stack.append(int(tokens[i]))
        return current_result


        

        