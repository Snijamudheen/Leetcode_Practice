# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

       n = len(matrix) 

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        then next step:
        matrix = [
            [1, 4, 7],
            [2, 5, 6],
            [3, 8, 9]
        ] we only swapped 2 with 4 and 3 with 7, 1 is still at the same place (thats why range is i+1)

        and after going thru the loop...finally we get the transpose which is 
        matrix = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ] but this is not what we want, we need to reverse each row meaning, row 1,4,7 becomes 7,4,1

        so final step we get:
        matrix = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
"""
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


-------------------------------------------------------------------------------------------------------------

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                # Swap across the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
