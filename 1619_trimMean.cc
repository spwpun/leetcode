#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double trimMean(vector<int>& arr) {
        double mean = 0.0;
        sort(arr.begin(), arr.end());
        int length = arr.size() / 20;
        // remove the first element
        arr.erase(arr.begin(), arr.begin() + length);
        arr.erase(arr.end() - length, arr.end());
        int sum = 0;
        for (int num: arr) {
            sum += num;
        }
        mean = sum/(double)arr.size();
        
        return mean;
    }
};

int main() {
    Solution s;
    vector<int> arr = {6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4};
    cout << s.trimMean(arr) << endl;
    return 0;
}