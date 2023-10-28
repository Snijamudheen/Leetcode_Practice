/*We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.*/

 bool detectCapitalUse(string word) {
 
           if(word[0]<'a'){                                                 //** first letter capital
              int cap = 0;
              for(int i =0;i<word.size();i++)if(word[i]<'a')cap++;
              if(cap>1 && cap< word.size())return false;                    //** more than 1 capital and less than word length
           }
           else
               for(int i =0;i<word.size();i++)if(word[i]<'a')return false;  //*** return false if any capital found 
               
           return true;
    }
