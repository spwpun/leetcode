#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        reverse_str = str(x)[::-1]
        flag = False
        if '-' in reverse_str:
            reverse_str = reverse_str[:-1]
            flag = True
        res = int(reverse_str, 10)
        if flag and res > 2**31:
            res = 0
        elif not flag and res >= 2**31:
            res = 0
        elif flag:
            res = - res
        
        return res
# @lc code=end

