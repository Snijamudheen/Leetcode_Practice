'''On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
The knight continues moving until it has made exactly k moves or has moved off the chessboard.
Return the probability that the knight remains on the board after it has stopped moving.'''

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        from functools import lru_cache

        moves = [  # Knight's 8 possible moves
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        @lru_cache(None)
        def dfs(r, c, steps_left):
            # If out of bounds or out of the board, no chance
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
                
            # If no more moves left, it's a valid path
            if steps_left == 0:
                return 1

            prob = 0
            for dr, dc in moves:
                prob += dfs(r + dr, c + dc, steps_left - 1)

            return prob / 8  # average probability

        return dfs(row, column, k)
