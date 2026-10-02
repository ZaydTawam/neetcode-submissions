class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        visited = set()

        def backtrack(index, board_pos):
            if index == len(word):
                return True

            r, c = board_pos
            deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in deltas:
                nr, nc = r + dr, c + dc
                
                if not 0 <= nr < num_rows or not 0 <= nc < num_cols:
                    continue
                
                if (nr, nc) in visited:
                    continue

                if board[nr][nc] == word[index]:
                    visited.add((nr, nc))
                    if backtrack(index + 1, (nr, nc)):
                        return True
                    visited.remove((nr, nc))
            
            return False
        
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == word[0]:
                    visited.add((row, col))
                    if backtrack(1, (row, col)):
                        return True
                    visited.remove((row, col))
        
        return False