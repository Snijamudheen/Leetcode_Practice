/*Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.*/

class Solution 
{
    public:
        bool isValid(string s) 
        {
            stack<char> bracket;
            
            for (char& c : s) 
            {
                switch (c) 
                {
                    case '(': 
                        bracket.push(c); 
                        break;
                        
                    case '{': 
                        bracket.push(c); 
                        break;
                        
                    case '[': 
                        bracket.push(c); 
                        break;
                        
                    case ')': 
                        if (bracket.empty() || bracket.top() != '(') 
                            return false; 
                        else 
                            bracket.pop(); 
                        break;
                        
                    case '}': 
                        if (bracket.empty() || bracket.top() != '{') 
                            return false; 
                        else 
                            bracket.pop(); 
                        break;
                        
                    case ']': 
                        if (bracket.empty() || bracket.top() != '[') 
                            return false; 
                        else 
                            bracket.pop(); 
                        break;     
                }
            }
            return bracket.empty();
        }  
};
