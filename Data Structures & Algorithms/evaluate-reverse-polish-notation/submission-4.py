class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            print(operands)
            if token == '+':
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(operand1 + operand2)
            elif token == '-':
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(operand1 - operand2)
            elif token == '*':
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(operand1 * operand2)
            elif token == '/':
                operand2 = operands.pop()
                operand1 = operands.pop()
                operands.append(int(operand1 / operand2))
            else:
                operands.append(int(token))
        return operands[0]