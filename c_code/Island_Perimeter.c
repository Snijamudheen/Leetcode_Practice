/*You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, 
width and height don't exceed 100. Determine the perimeter of the island.*/

class Solution 
{
  public:
      int islandPerimeter(vector<vector<int>>& grid) 
      {
          int m = grid.size(); //row
          int n = grid[0].size(); //column
          int ans = 0;

          for(int i = 0; i < m; i++)
          {
              for(int j = 0; j < n; j++)
              {
                  if(grid[i][j] == 1)
                  { 
                    ans += 4; 

                   if( i+1 <m  && grid[i+1][j] == 1  )  // if down neighbour is there
                   {        
                            ans--;}
                 if(   i-1 >=0 && grid[i-1][j] == 1 ) // if upward neighbour is there
                 { ans--;}
                   if(   j-1>=0  && grid[i][j-1] == 1)  // if left neighbour is there
                   {     ans--;}
                 if(  j+1<n && grid[i][j+1] == 1 ) // if right neighbour is there
                 { ans--;}
                }
              }
          }
          return ans;
      }
};
