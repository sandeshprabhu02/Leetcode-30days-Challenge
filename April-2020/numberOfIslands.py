"""
Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count=0
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(row) for _ in range(col)]]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self._dfs(grid, visited, row, col, i, j)
                    count += 1
        return count
    
    def _dfs(self, grid, visited, row, col, i, j):
        if i<0 or j<0 or i>=row or j>=col or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        # visited[i][j] = True
        #check all 4 sides
        self._dfs(grid, visited, row, col, i+1, j)
        self._dfs(grid, visited, row, col, i-1, j)
        self._dfs(grid, visited, row, col, i, j+1)
        self._dfs(grid, visited, row, col, i, j-1)


print(Solution().numIslands([
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']]))