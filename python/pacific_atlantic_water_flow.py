# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the grid
        ROWS, COLS = len(heights), len(heights[0])

        # Create sets to keep track of cells that can flow to each ocean
        pac, atl = set(), set()

        # Helper function to perform depth-first search (DFS), visit can be pac or atl, prevHeight is neighbor
        def dfs(r, c, visit, prevHeight):
            # Stop if the cell is already visited or if it's out of bounds
            if (
                (r, c) in visit or   # Cell has already been visited
                r < 0 or c < 0 or    # Cell is out of bounds (top/left edges)
                r == ROWS or c == COLS or  # Cell is out of bounds (bottom/right edges)
                heights[r][c] < prevHeight  # Water can't flow uphill, current cell < neighbor cell so no
            ):
                return

            # Mark this cell as visited
            visit.add((r, c))

            # Explore the neighbors in all 4 directions
            dfs(r + 1, c, visit, heights[r][c])  # Move Down
            dfs(r - 1, c, visit, heights[r][c])  # Move Up
            dfs(r, c + 1, visit, heights[r][c])  # Move Right
            dfs(r, c - 1, visit, heights[r][c])  # Move Left

        # Run DFS for the Pacific Ocean starting from the top row and left column
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])  # Top row (Pacific), going thru the first row, meaning only the first values of all the columns
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # Bottom row (Atlantic), going thru last row, meaning only the last values of all the columns

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])  # Left column (Pacific), going thru the first col, meaning only the first values of all the rows
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # Right column (Atlantic), going thru last col, meaning only the last values of all the rows

        # Create the result list to store cells that can flow to both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                # If a cell is in both sets (can reach both oceans), add it to the result
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        # Return the result
        return res
