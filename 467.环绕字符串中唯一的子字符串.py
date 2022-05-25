#
# @lc app=leetcode.cn id=467 lang=python3
#
# [467] 环绕字符串中唯一的子字符串
#
# 思路：动态规划，寻找一个字符串的所有字串，判断有多少个环绕字符串

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        if len(p) == 1:
            return 1
        dp = [0] * 26
        k = 0
        for i in range(0, len(p)):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[ord(p[i]) - ord("a")] = max(dp[ord(p[i]) - ord("a")], k)
   
        return sum(dp)
# Test
# p = "zaba"
# s = Solution()
# print(s.findSubstringInWraproundString(p))
# @lc code=end

