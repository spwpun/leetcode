// g++ 1582.矩阵中的特殊位置.cc -o numSpecial -std=c++11 && ./numSpecial
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        if (mat.size() == 0) {
            return 0;
        }
        
        int cnt = 0;

        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[0].size(); j++) {
                if (mat[i][j] == 1) {
                    if (count(mat[i].begin(), mat[i].end(),  1) > 1) break;
                    int col_cnt = 0;
                    for (int k = 0; k < mat.size(); k++) {
                        if (mat[k][j] == 1) col_cnt++;
                    }
                    if (col_cnt == 1) cnt++;
                    else break;
                }
            }
        }

        return cnt;

    }
};

int main() {
    vector<vector<int>> mat = {{1,0,0},{0,0,1},{1,0,0}};
    Solution s;
    cout << s.numSpecial(mat) << endl; // The answer is 1
    return 0;
}