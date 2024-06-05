/* Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.*/

class Solution 
{
    public:
        bool isLongPressedName(string name, string typed) 
        {  
            int i = 0, m = name.length(), n = typed.length();
            
            for (int j = 0; j < n; ++j)
                if (i < m && name[i] == typed[j])
                    ++i;
                else if (!j || typed[j] != typed[j - 1])
                    return false;

            return i == m;
        }
};
