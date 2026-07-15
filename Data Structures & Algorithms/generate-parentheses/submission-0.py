class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_strs = []

        def backtrack(path, num_opening):
            if len(path) == n*2:
                valid_strs.append(path)
                return
            
            if num_opening:
                path += ")"
                backtrack(path, num_opening - 1)
                path = path[:len(path) - 1]
            
            if n*2 - len(path) >= 2 + num_opening:
                path += "("
                backtrack(path, num_opening + 1)
                path = path[:len(path) - 1]

        backtrack("", 0)
        return valid_strs