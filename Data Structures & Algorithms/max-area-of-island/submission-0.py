class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_adj_cells(cell):
            r, c = cell
            deltas = [(1,0), (-1,0), (0,1), (0,-1)]

            adj_cells = []
            for r_delta, c_delta in deltas:
                new_r = r + r_delta
                new_c = c + c_delta
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                    adj_cells.append((new_r, new_c))
            
            return adj_cells

        def get_island_size(start):
            size = 0
            curr_lvl = [start]

            while curr_lvl:
                next_lvl = []
                for cell in curr_lvl:
                    size += 1
                    for r, c in get_adj_cells(cell):
                        grid[r][c] = 0
                        next_lvl.append((r,c))
                curr_lvl = next_lvl
            
            return size
        
        max_size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_size = max(max_size, get_island_size((r, c)))
        
        return max_size