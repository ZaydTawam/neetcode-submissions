class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        l_diags_taken = set()
        r_diags_taken = set()
        cols_taken = set()

        def backtrack(positions):
            if len(positions) == n:
                solution = []
                for _, col in positions:
                    solution.append("."*col + "Q"+ "."*(n-col-1))
                solutions.append(solution)
                return
            
            for i in range(n):
                row, col = len(positions), i
                if col in cols_taken or (row - col) in r_diags_taken or (row + col) in l_diags_taken:
                    continue
                positions.append((row, col))
                l_diags_taken.add(row + col)
                r_diags_taken.add(row - col)
                cols_taken.add(col)
                backtrack(positions)
                positions.pop()
                l_diags_taken.remove(row + col)
                r_diags_taken.remove(row - col)
                cols_taken.remove(col)
            
        
        backtrack([])
        return solutions


# 0 0
#     1 2 X
#       2 X
#     1 3 X
#       2 1 X
#           3 X
# 0 1
#     1 3
#       2 0
#           3 2 

# .Q..
# ...Q
# Q...
# ..Q.