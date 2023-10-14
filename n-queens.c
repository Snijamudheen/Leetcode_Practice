/*The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.*/

class Solution 
{
    public:
        bool safe(int row, vector<string>& board, int col, int n)
        {
            int x = row;
            int y = col;
            
            while(y >= 0)
            {
                if(board[x][y] == 'Q')
                {
                    return false;
                }
                y--;
            }
            
            x = row;
            y = col;
            
            while(x >= 0 && y >= 0)
            {
                if(board[x][y] == 'Q') 
                    return false;
                x--;
                y--;
            }
            
            x = row;
            y = col;
            
            while(y >= 0 && x < n)
            {
                if(board[x][y] == 'Q')
                    return false;
                x++;
                y--;
            }
            return true;
        }
    
        void add(vector<string>& board, vector<vector<string>>& ans, int n)
        {
            vector<string> temp;
    
            for(int i = 0; i < n ; i++)
            {
                temp.push_back(board[i]);
            }
            ans.push_back(temp);
        }
    
        void solve(int col, vector<string>& board, vector<vector<string>>& ans, int n)
        {
            if(col >= n)
            {
                add(board, ans, n);
                return;
            }
    
            for(int i = 0; i < n; i++)
            {
                if(safe(i, board, col, n))
                {
                    board[i][col] = 'Q';
                    solve(col + 1, board, ans, n);
                    board[i][col] = '.';
                }
            }
        }
         
        vector<vector<string>> solveNQueens(int n) 
        {
            string x = "";
            
            for(int j = 0; j < n; j++)
            {
                x += '.';
            }
            
            vector<string> board(n , x);
            vector<vector<string>> ans;
    
            solve(0, board, ans, n);
            return ans;
        }
};
