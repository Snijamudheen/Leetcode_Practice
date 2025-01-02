# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

      
        # matrix = [
        #    [1, 2, 3],   # 3 columns
        #    [4, 5, 6],
        #    [7, 8, 9]
        #   ]
        # len(matrix[0]) = 3

        left, right = 0, len(matrix[0]) # changing columns
        top, bottom = 0, len(matrix) # changing rows

        while left < right and top < bottom:
            # top to right (left to right)
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1 # going downwards after finishing top row

            # right to bottom (top to bottom)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1 # going leftwards cuz right pointer is out of bounds

            # Exit the loop if there are no rows/columns left
            if not (left < right and top < bottom):
                break

            # right to bottom (right to left), opposite direction
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i]) #bottom is out of bounds so bottom -1
            bottom -= 1 # going upwards since we finshed the bottommost row

            # bottom to left (bottom to top), opposite direction
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 # going right so left + 1
        return res
