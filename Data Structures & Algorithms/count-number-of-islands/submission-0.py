class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if not grid:
            return 0
        # get dimensions of grid
        rows, columns = len(grid), len(grid[0])
        # mark positions/ cells visited
        visit = set()
        islands = 0

        # iterative so u need to use a data structure (bfs uses queue)
        def bfs(r,c):
            # create queue
            q = collections.deque()
            # add cell to visit
            visit.add((r,c))
            # add cell to queue
            q.append((r,c))
            # while queue not empty expand island
            while q:
                # pop from queue
                row, column = q.popleft()
                # check adjacent positions of cells [right, left, above, below]
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                # for each of these directions
                # check position is in bounds (first 2), 
                # check if its a land position( needs to == 1) and 
                # check that position hasnt been visited
                for dr, dc in directions:
                    r, c = row + dr, column + dc
                    if (r in range(rows) and 
                        c in range(columns) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        # add to our queue so we have to run bfs on this cell
                        q.append((r, c))
                        # mark as visited
                        visit.add((r, c))
                
        # visit every position in the grid
        for r in range(rows):
            for c in range(columns):
                # if we visit a 0, do nothing
                # but if u visit a 1 then u have to traverse and mark as visited
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands +=1
        return islands

# if u get asked dfs, change popleft to popright itll pop most recent element but itll be iterative 