/*Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], 
we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.*/

class Solution 
{
  public:
      int findContentChildren(vector<int>& g, vector<int>& s) 
{
          int n = g.size(), m = s.size(),cnt = 0,i = 0;
          priority_queue<int> pq1;
  
          for (int i = 0; i < n; i++) 
            pq1.push(g[i]);
  
          priority_queue<int> pq2;
  
          for (int i = 0; i < m; i++) 
            pq2.push(s[i]);
  
          while(i < g.size())
          {
            if (pq1.empty() || pq2.empty()) 
              break;
            else if(pq1.top() <= pq2.top())
              cnt++, pq1.pop(), pq2.pop();
            else if(pq1.top() > pq2.top()) 
              pq1.pop();
            i++;
          }
          return cnt;
      }
};
