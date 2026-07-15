class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def backtrack(index, coords):
            if index == len(word) - 1:
                return True

            res = False
            
            row, col = coords
            deltas = [(0,1), (0,-1), (1,0), (-1,0)]
            for row_delta, col_delta in deltas:
                new_row = row + row_delta
                new_col = col + col_delta
                if not 0 <= new_row < len(board) or not 0 <= new_col < len(board[0]):
                    continue
                new_coords = (new_row, new_col)
                if new_coords in visited:
                    continue
                if board[new_row][new_col] != word[index + 1]:
                    continue
                visited.add(new_coords)
                res = backtrack(index + 1, new_coords)
                if res:
                    return True
                visited.remove(new_coords)

            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != word[0]:
                    continue
                visited.add((row, col))
                if backtrack(0, (row, col)):
                    return True
                visited.remove((row, col))
        return False