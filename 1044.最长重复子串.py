#
# @lc app=leetcode.cn id=1044 lang=python3
#
# [1044] 最长重复子串
#

# @lc code=start
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            while s[i:i+len(ans)+1] in s[i+1:]:
                ans = s[i:i+len(ans) + 1]
        return ans

# Test
# s = "abcbbbbdca"
# print(Solution().longestDupSubstring(s))
# @lc code=end

