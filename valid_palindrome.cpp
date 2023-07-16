/*A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.*/

class Solution 
{
	public:
	    	bool isPalindrome(string s) 
		{
		        string result = "";
		        
		        for(int i = 0; i < s.size(); i++)
			{
				if((s[i] - 'a' >= 0 && s[i] - 'a' <= 25) ||  
				(s[i] - 'A' >= 0 && s[i] - 'A' <= 25) ||  
				(s[i] - 48 >= 0 && s[i] - 48 <= 9))
				{   
		                	result += tolower(s[i]); 
		           	}
		        }
		        return checkPalindrome(result);
	    	}
	    
	   	bool checkPalindrome(string s)
		{
		        for(int left = 0, right = s.size() - 1; left < right; left++, right--)
			{
		            if(s[left] != s[right]) 
				return false;
			}
	        	return true;
	    	}
};
