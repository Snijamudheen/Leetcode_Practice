'''Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).
Note: You can only move left, right, up and down, and only through cells that contain 1.'''


from collections import deque

def shortestDistance(N, M, X, Y, A):
    # If starting cell is 0, can't move
    if A[0][0] == 0:
        return -1

    # Movement directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Create an empty list to hold the rows
    visited = []

    # Loop through each row (N times)
    for i in range(N):
        # Create one row with M False values
        row = []
        for j in range(M):
            row.append(False)  # Not visited yet
        # Add this row to the main visited list
        visited.append(row)

    # Mark the starting point as visited
    visited[0][0] = True

    # BFS queue: each item is (row, col, steps)
    q = deque()
    q.append((0, 0, 0))

    # Start BFS
    while q:
        i, j, steps = q.popleft()

        # If we reached the target
        if i == X and j == Y:
            return steps

        # Check all 4 directions
        for dx, dy in directions:
            ni, nj = i + dx, j + dy

            # Check bounds and if it's walkable and not visited
            if 0 <= ni < N and 0 <= nj < M and A[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj, steps + 1))

    # Target not reachable
    return -1
