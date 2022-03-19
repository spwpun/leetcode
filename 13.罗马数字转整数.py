#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
# 比较当前的字符和下一个字符的大小，出现特例就转换
#

# @lc code=start
class Solution:
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    def romanToInt(self, s: str) -> int:
        num = 0
        i = 0
        while i < len(s): 
            if (i != len(s) - 1) and self.map[s[i]] < self.map[s[i+1]]:
                num += self.map[s[i+1]] - self.map[s[i]]
                i += 1
            else:
                num += self.map[s[i]]
            
            i += 1
        
        return num
# @lc code=end

