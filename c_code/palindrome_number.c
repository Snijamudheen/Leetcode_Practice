/*Given an integer x, return true if x is a palindrome integer. An integer is a palindrome when it reads the same backward as forward.*/

class Solution 
{
    public:
        bool isPalindrome(int x) 
        { 
               int r, m;
               int long long rev = 0;
            
                m = x;
                while(x > 0)
                {
                       rev = rev * 10 + x % 10;
                        x = x / 10;
                }

                if(m == rev)
                {
                   return true;
                }

                return false;
        }
};
