/*Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.*/

class Solution 
{
  public:
    bool wordPattern(string pattern, string s) 
    {
        int n = pattern.size();
        stringstream str(s);
        string word;
        vector<string> words;
      
        while(str>>word)
            words.push_back(word);
      
        if(pattern.size() != words.size())
            return false;
      
        map <char, string> charToString;
        map <string, char> stringToChar;
      
        for(int i = 0; i < n; i++) 
        {
            if(charToString.find(pattern[i]) == charToString.end() &&
              stringToChar.find(words[i]) == stringToChar.end())
            {
                    charToString[pattern[i]] = words[i];
                    stringToChar[words[i]] = pattern[i];
            }
            else if(charToString[pattern[i]] != words[i])
                return false;
        }
        return true;
    }
};
