#include <iostream>
#include <sstream>
using namespace std;

class Solution {
public:
    int maximumSwap(int num) {
        // convert a num to a string
        stringstream ss;
        ss << num;
        string s = ss.str();
        vector<int> nums(s.size());
        for (int v = 0; v < s.size(); v++)
        {    // traverse the string
            int max = s[v];
            int max_index = v;
            for (int i = v + 1; i < s.size(); i++) {
                if (s[i] >= max) {
                    max = s[i];
                    max_index = i;
                }
            }
            if (max_index == v) {
                nums.push_back(num);
            }
            else {
                // swap the first and the max
                string temp = s;
                char tmp = temp[v];
                temp[v] = temp[max_index];
                temp[max_index] = tmp;
                // convert the string to a num
                stringstream ss2;
                ss2 << temp;
                int res;
                ss2 >> res;
                nums.push_back(res);
            }
        }
        // find the max
        int max = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        return max;
    }

};

int main() {
    Solution s;
    cout << s.maximumSwap(2736) << endl;
    cout << s.maximumSwap(9973) << endl;
    cout << s.maximumSwap(98368) << endl;
    cout << s.maximumSwap(1993) << endl;
    return 0;
}