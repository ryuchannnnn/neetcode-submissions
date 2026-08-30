class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get rows and columns of the graph
        rows, columns = len(grid), len(grid[0])
        visit = set()
        # 
        def dfs(r,c):
            # base case out of bounds for either row or columbs, row or columns is too big, or we reach water
            # or we already visited a position
            if (r < 0 or r == rows or c < 0 or c == columns or grid[r][c] == 0 or (r,c) in visit):
                return 0
            # add to set since we visited it
            visit.add((r,c))
            # calculate the area of the island by running dfs on all 4 directions
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))
        area = 0
        # iterate over entire grid 
        for r in range(rows):
            for c in range(columns):
                area = max(area, dfs(r,c))

        return area