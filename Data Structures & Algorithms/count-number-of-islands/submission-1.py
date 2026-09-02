class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_adj_lands(coords):
            row, col = coords
            deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            adj_lands = []
            for row_delta, col_delta in deltas:
                new_row = row + row_delta
                new_col = col + col_delta

                if not 0 <= new_row < len(grid) or not 0 <= new_col < len(grid[0]):
                    continue
                if grid[new_row][new_col] == "0":
                    continue
                
                adj_lands.append((new_row, new_col))
            
            return adj_lands

        def remove_island(start):
            curr_lvl = [start]
            while curr_lvl:
                next_lvl = []
                for coords in curr_lvl:
                    for row, col in get_adj_lands(coords):
                        grid[row][col] = "0"
                        next_lvl.append((row, col))

                curr_lvl = next_lvl
        
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    num_islands += 1
                    grid[row][col] = "0"
                    remove_island((row, col))
        
        return num_islands
