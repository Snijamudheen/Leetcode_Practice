/*Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
You must write an algorithm that runs in logarithmic time.*/

class Solution 
{
    public:
        int hIndex(vector<int>& citations) 
        {
            int n = citations.size();
            int low = 0, high = n - 1;
            int ans = 0;
            
            while(low <= high)
            {
                int mid = low + (high - low) / 2;

                if(citations[mid] >= n - mid)
                {
                    ans = max(ans, n - mid);
                    high = mid - 1;
                }
                else
                {
                    low = mid + 1;
                }
            }
            return ans;
        }
};
