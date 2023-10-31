/*You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
 */

class Solution {
public:
    bool canPlaceFlowers(vector<int>& v, int n) {
        if(n==0)return true;
        if(v.size()==1){
            if((v[0]==0&&n==1)||n==0)return true;
            return false;
        }if(v.size()==2){
            if(n==0||(n==1&&(v[0]==0&&v[1]==0))){
                return true;
            }return false;
        }
        if(v[0]==0&&v[1]==0){
            v[0]=1;
            n--;
        }if(n==0)return true;
        for(int i = 1; i < v.size()-1; i++){
            if(v[i-1]==1)continue;
            if(v[i]==0&&v[i+1]==0){
                v[i] = 1;
                n--;
            }
                if(n==0)return true;
        }
                if(n==0)return true;
        if(n==1){
            if(v[v.size()-2]==0&&v[v.size()-1]==0){
                return true;
            }
            return false;
        }
        return false;
    }
};
