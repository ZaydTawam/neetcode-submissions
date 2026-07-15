class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(':
                stk.append('(')
            elif c == '{':
                stk.append('{')
            elif c == '[':
                stk.append('[')
            elif c == ')':
                if not stk or stk[-1] != '(':
                    return False
                stk.pop()
            elif c == '}':
                if not stk or stk[-1] != '{':
                    return False
                stk.pop()
            elif c == ']':
                if not stk or stk[-1] != '[':
                    return False
                stk.pop()
        
        return not stk