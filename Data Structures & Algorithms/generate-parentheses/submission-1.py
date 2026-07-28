class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_strs = []
        def backtrack(s, num_opening):
            if len(s) == n*2:
                valid_strs.append(''.join(s))
                return 
                        
            if num_opening < n:
                s.append('(')
                backtrack(s, num_opening + 1)
                s.pop()

            if len(s) - num_opening < num_opening:
                s.append(')')
                backtrack(s, num_opening)
                s.pop()
                
        backtrack([],0)
        return valid_strs
