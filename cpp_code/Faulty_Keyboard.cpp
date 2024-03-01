/*Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.
You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.
Return the final string that will be present on your laptop screen.*/

class Solution 
{
  public:
      string finalString(string s) 
      {
          string ans;

          for(char c : s)
          {
              if(c == 'i') 
                  reverse(ans.begin(),ans.end());
              else 
                  ans+=c;
          }
          return ans;
      }
};
