'''There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n #bottom row that is always 1
        
        for i in range(m-1): #all row except last one thats y it is m-1
            newrow = [1] * n #the new row above the bottom row, initialize the same values
            for j in range(n-2, -1, -1): # (edge case) go thru all values in row except last since it is 1, right to left, in reverse
                newrow[j] = newrow[j+1] + row[j] #right value + down row value
            row = newrow #update new row
        return row[0] #final vlaue in first block
