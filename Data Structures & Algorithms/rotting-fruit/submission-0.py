def get_adj_fresh(coords, grid):
    num_rows, num_cols = len(grid), len(grid[0])
    row, col = coords
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    adj_fresh = []

    # computing and checking all adjacent cells
    for row_delta, col_delta in deltas:
        new_row = row + row_delta
        new_col = col + col_delta

        # boundary check
        if not 0 <= new_row < num_rows or not 0 <= new_col < num_cols:
            continue
        
        # add fresh oranges to output
        if grid[new_row][new_col] == 1:
            adj_fresh.append((new_row, new_col))
    
    return adj_fresh

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        minutes = 0
        fresh_count = 0
        curr_lvl = []

        # get all initial rotten positions and count fresh
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    curr_lvl.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        # continue rotting until no more fresh oranges
        while curr_lvl:
            next_lvl = []
            for orange in curr_lvl:
                for row, col in get_adj_fresh(orange, grid):
                    grid[row][col] = 2
                    fresh_count -= 1
                    next_lvl.append((row, col))
            if next_lvl:
                minutes += 1
            curr_lvl = next_lvl
        
        if fresh_count != 0:
            return -1
        
        return minutes
