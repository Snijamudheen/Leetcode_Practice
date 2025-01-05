# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Step 1: Get the number of rows and columns in the matrix
        # ROWS = number of rows in the matrix
        # COLS = number of columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Step 2: Create a flag to track if the first row needs to be set to zero
        # We can't use the first row to mark itself, so we use this variable.
        rowZero = False  # This will be True if any cell in the first row is 0.

        # Step 3: Figure out which rows and columns need to be set to zero
        # We’ll loop through every cell in the matrix.
        # If we find a zero, we’ll use the first row and first column to mark it.
        for r in range(ROWS):  # Loop through each row
            for c in range(COLS):  # Loop through each column
                if matrix[r][c] == 0:  # If we find a zero in the matrix
                    # Mark the top of the current column with a zero
                    # This tells us that this column needs to be zeroed out later.
                    matrix[0][c] = 0

                    # If the zero is not in the first row, mark the start of the row
                    if r > 0:
                        # Mark the first cell of the current row with a zero
                        # This tells us that this row needs to be zeroed out later.
                        matrix[r][0] = 0
                    else:
                        # If the zero is in the first row, set the rowZero flag to True
                        # We’ll handle the first row separately later.
                        rowZero = True

        # Step 4: Use the markers to set the appropriate cells to zero
        # We’ve already marked the first row and first column.
        # Now we use those markers to zero out the rest of the matrix.

        # Start from row 1 and column 1 to avoid messing with our markers.
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # If the marker in the top row or the marker in the first column is zero,
                # that means this cell needs to be zeroed out.
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    # Set the current cell to zero
                    matrix[r][c] = 0

        # Step 5: Handle the first column separately
        # We use the top-left cell (matrix[0][0]) to mark whether the first column needs to be zeroed.
        if matrix[0][0] == 0:
            # If the top-left cell is zero, set the entire first column to zero.
            for r in range(ROWS):
                matrix[r][0] = 0

        # Step 6: Handle the first row separately
        # If rowZero is True, it means the first row needs to be zeroed out.
        if rowZero:
            # Set every cell in the first row to zero
            for c in range(COLS):
                matrix[0][c] = 0
