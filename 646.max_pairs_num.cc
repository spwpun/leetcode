#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end(), [](const vector<int>& a, const vector<int>& b){
            return a[1] < b[1];
        });
        int res = 0;
        int cur = INT_MIN;
        for (auto& p: pairs) {
            if (p[0] > cur) {
                cur = p[1];
                res++;
            }
        }

        return res;
    }
};

int main() {
    Solution s;
    vector<vector<int>> pairs = {{-6,9},{1,6},{8,10},{-1,4},{-6,-2},{-9,8},{-5,3},{0,3}};
    cout << s.findLongestChain(pairs) << endl;
    return 0;
}