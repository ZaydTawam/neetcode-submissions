class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_adj_cells(cell):
            r, c = cell
            deltas = [(1,0), (-1,0), (0,1), (0,-1)]

            adj_cells = []
            for r_delta, c_delta in deltas:
                new_r = r + r_delta
                new_c = c + c_delta
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == "1":
                    adj_cells.append((new_r, new_c))
            
            return adj_cells

        def remove_island(start):
            curr_lvl = [start]

            while curr_lvl:
                next_lvl = []
                for cell in curr_lvl:
                    for r, c in get_adj_cells(cell):
                        grid[r][c] = "0"
                        next_lvl.append((r,c))
                curr_lvl = next_lvl
        
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    island_count += 1
                    grid[r][c] = "0"
                    remove_island((r, c))
        
        return island_count