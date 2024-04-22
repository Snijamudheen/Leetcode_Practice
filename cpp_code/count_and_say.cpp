/*The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. 
Finally, concatenate every said digit.*/

string m[31] = {""};
class Solution 
{
	public:
	    string countAndSay(int n) 
	    {
	        m[1] = "1";
	        string next, prev;
	        int i, j, len;
			
		//generating the say(i)
	        for(i = 2; i < n + 1; i++)
	        {
	            if(m[i] != "")
	                continue;
			
	            next = "";
	            prev = m[i - 1];
	            len = prev.size();
	            int count = 1;
				
		//reading out the say(i-1) i.i string prev
	            for(j = 1; j < len; j++)
	            {
	                if(prev[j - 1] == prev[j])
	                    count++;
	                else
	                {
	                    next = next + to_string(count) + prev[j - 1];
	                    count = 1;
	                }
	                
	            }
	            next = next + to_string(count) + prev[j - 1];
	            m[i] = next;
	        }
	        return m[n];
	    }
};
