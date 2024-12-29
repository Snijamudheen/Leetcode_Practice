# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the number of rows (m) and columns (n) in the grid
        m, n = len(grid), len(grid[0]) 

        # The DFS (Depth-First Search) function is used to "explore" an island and mark all its connected lands as visited.
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1': # If the current cell is out of bounds or it's water ('0'), stop the recursion.
                return
            else:
                grid[i][j] = '0' # Convert the current land ('1') to water ('0') to mark it as visited. This prevents counting the same land multiple times.
                dfs(i, j+1)  # Explore right - adjacent cells
                dfs(i+1, j)  # Explore down
                dfs(i, j-1)  # Explore left
                dfs(i-1, j)  # Explore up

        numislands = 0
        # Loop through every cell in the grid.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    numislands += 1
                    dfs(i, j) # Use DFS to mark the entire island as visited

        return numislands
