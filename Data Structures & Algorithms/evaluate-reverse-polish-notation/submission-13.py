class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == "+":
                operand2 = stk.pop()
                operand1 = stk.pop()
                stk.append(operand1 + operand2)
            elif token == "-":
                operand2 = stk.pop()
                operand1 = stk.pop()
                stk.append(operand1 - operand2)
            elif token == "*":
                operand2 = stk.pop()
                operand1 = stk.pop()
                stk.append(operand1 * operand2)
            elif token == "/":
                operand2 = stk.pop()
                operand1 = stk.pop()
                stk.append(int(operand1/operand2))
            else:
                stk.append(int(token))
        return stk.pop()