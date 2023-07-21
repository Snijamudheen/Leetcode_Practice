/*Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
For example, swapping at indices 0 and 2 in "abcd" results in "cbad".*/

class Solution 
{
  public:
        bool buddyStrings(string A, string B)
        {
          if (A.length() != B.length()) 
            return false;
          if (A == B && set<char>(A.begin(), A.end()).size() < A.size()) 
            return true;

          vector<int> dif;

          for (int i = 0; i < A.length(); ++i) 
            if (A[i] != B[i]) 
              dif.push_back(i);

          return dif.size() == 2 && A[dif[0]] == B[dif[1]] && A[dif[1]] == B[dif[0]];
        }
};
