class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        occupied_columns = set() 
        occupied_diag1 = set()
        occupied_diag2 = set()

        def backtrack(positions):
            if len(positions) == n:
                solution = []
                for col in positions:
                    solution.append("."*col + "Q" + "."*(n-col-1))
                solutions.append(solution)
                return
            
            for col in range(n):
                diagonal1, diagonal2 = len(positions) - col, len(positions) + col
                if col in occupied_columns or diagonal1 in occupied_diag1 or diagonal2 in occupied_diag2:
                    continue
                occupied_columns.add(col)
                occupied_diag1.add(diagonal1)
                occupied_diag2.add(diagonal2)
                positions.append(col)
                backtrack(positions)
                occupied_columns.remove(col)
                occupied_diag1.remove(diagonal1)
                occupied_diag2.remove(diagonal2)
                positions.pop()

        backtrack([])
        return solutions