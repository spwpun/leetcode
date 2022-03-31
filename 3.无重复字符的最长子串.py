#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ''
        max_len = 0

        for ch in s:
            if ch not in sub_str:
                sub_str += ch
            else:
                while True:
                    sub_str = sub_str[1:]
                    if ch not in sub_str:
                        break
                sub_str += ch
            # print("[Debug]Sub string:", sub_str, len(sub_str))
            c_len = len(sub_str)
            if c_len > max_len:
                max_len = c_len        
                
        return max_len
            
# @lc code=end

