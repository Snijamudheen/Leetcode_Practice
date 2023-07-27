/*An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.*/

class Solution 
{
  public:
      bool isUgly(int n) 
      {
          if(!n) 
            return false;
          
          while(!(n%2))
              n/=2;
  
          while(!(n%3))
              n/=3;
  
          while(!(n%5))
              n/=5;
          
          if(n==1) 
            return true;

          return false;
      }
};
