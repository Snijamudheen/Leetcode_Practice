/*Given a non-negative integer x, compute and return the square root of x. Since the return type is an integer, the decimal digits are truncated, and only the 
integer part of the result is returned. Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.*/

class Solution 
{
    public:
        int mySqrt(int x) 
        {
            if(x == 0 || x == 1)
                return x;
            
            long long start = 1;
            long long end = x;
            
            while(start <= end)
            {
                long long mid = start + (end - start) / 2;
                
                if(mid * mid <= x && (mid + 1) * (mid + 1) > x)
                    return mid;
                else if(mid * mid > x)
                    end = mid - 1;
                else if(mid * mid < x)
                    start = mid + 1;
            }
        
            return -1;
        }
};
