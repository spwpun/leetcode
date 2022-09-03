#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int length = pushed.size();
        int pop_idx = 0;
        vector<int> stack;
        for (int i = 0; i < length; i++)
        {
            stack.push_back(pushed[i]);
            while (!stack.empty() && stack[stack.size() - 1] == popped[pop_idx]){
                stack.pop_back();
                pop_idx++;
            }
        }
        for (int j = 0; j < stack.size(); j++) cout << stack[j] << " ";
        cout << endl;
        return stack.empty();
    }
};

int main(){
    Solution s;
    vector<int> pushed = {1,2,3};
    vector<int> popped = {2,1,3};
    cout << s.validateStackSequences(pushed, popped) << endl;
    return 0;
}