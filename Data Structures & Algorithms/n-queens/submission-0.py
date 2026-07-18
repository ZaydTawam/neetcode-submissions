class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        def is_valid_position(positions, new_position):
            new_r, new_c = new_position
            for r, c in positions:
                if new_r == r or new_c == c:
                    return False
                delta_r, delta_c = abs(r - new_r), abs(c - new_c)
                if delta_r == delta_c:
                    return False
            return True

        def backtrack(positions):
            if len(positions) == n:
                solution = []
                for _, c in positions:
                    solution.append("."*c + "Q" + "."*(n-c-1))
                solutions.append(solution)
                return
            
            for i in range(n):
                new_position = (len(positions), i)
                if not is_valid_position(positions, new_position):
                    continue
                positions.append(new_position)
                backtrack(positions)
                positions.pop()

        backtrack([])
        return solutions