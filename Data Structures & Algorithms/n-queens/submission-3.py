class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        cols_taken = set()
        left_diag_taken = set()
        right_diag_taken = set()

        def backtrack(layout):
            print(layout)
            if len(layout) == n:
                solution = []
                for col in layout:
                    solution.append("."*col + "Q" + "."*(n - col - 1))
                solutions.append(solution)
                return
            
            for col in range(n):
                if col in cols_taken:
                    continue
                row = len(layout)
                if row + col in left_diag_taken:
                    continue
                if row - col in right_diag_taken:
                    continue
                cols_taken.add(col)
                left_diag_taken.add(row + col)
                right_diag_taken.add(row - col)
                layout.append(col)
                backtrack(layout)
                cols_taken.remove(col)
                left_diag_taken.remove(row + col)
                right_diag_taken.remove(row - col)
                layout.pop()

        backtrack([])
        return solutions

