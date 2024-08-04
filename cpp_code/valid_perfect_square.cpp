/*Given a positive integer num, write a function which returns True if num is a perfect square else False. Follow up: Do not use any built-in library function such as sqrt.*/

class Solution 
{
    public:
        bool isPerfectSquare(int num) 
        {
            for(int i = 1; i <= num; i++)
            {
                if(i*i == num) 
                    return true;
                if(i*i > num) 
                    return false;
            }
            return false;
        } 
};
