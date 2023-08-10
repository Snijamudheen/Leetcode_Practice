/*Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.*/

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        unordered_map<int, int>m;
        for(int i=0; i<nums.size(); i++){
            if(m.find(nums[i])==m.end()){
                m[nums[i]]++;
            }
            else{
                nums.erase(nums.begin()+i);
                i--;
            }
        }
        priority_queue<int, vector<int>, greater<int>>q;
        for(int i=0; i<nums.size(); i++){
            q.push(nums[i]);
            if(3<q.size()){
                q.pop();
            }
        }
        if(q.size()<3){
            return *max_element(nums.begin(), nums.end());
        }
        return q.top();
    }
};
