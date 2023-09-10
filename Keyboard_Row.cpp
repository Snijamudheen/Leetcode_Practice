/*Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 
Constraints:
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).*/

class Solution 
{
 public:
     vector<string> findWords(vector<string>& words) 
     {
         
         int s1 = 0, s2 = 0, s3 = 0;
         vector<string> ans;
      
         for( auto &&item:words)
         {
             int len = item.size();
             
             for(int i = 0; i < len; i++)
             {
                 char c = item[i];
              
                 if(c == 'A' || c == 'a' || c == 'S' || c == 's' || c == 'D' || c == 'd' || c == 'F' || c == 'f' || c == 'G' || c == 'g' || c == 'H' || c == 'h' || c =='J' || c == 'j' || c == 'K' || c == 'k' || c == 'L' || c == 'l')
                 {
                     //cout<<"Str1 :"<<item[i]<<endl;
                     s1++;
                 }
                 else if(c == 'Z' || c == 'z' || c == 'X' || c == 'x' || c == 'C' || c == 'c' || c == 'V' || c == 'v' || c == 'B' || c == 'b' || c == 'N' || c == 'n' || c == 'M' || c == 'm')
                 {
                     //cout<<"Str2 :"<<item[i]<<endl;
                     s2++;
                 }
                 else 
                 {
                     //cout<<"Str2 :"<<item[i]<<endl;
                     s3++;
                 }
             }
          
             if(s1 == len  || s2 == len || s3 == len)
             {
                 ans.push_back(item);
             }
          
             s1 = 0, s2 = 0, s3 = 0;
         }
         
           return ans;  
     }
};
