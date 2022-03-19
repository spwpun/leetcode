#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
# 比较的是字符，对str[0]按字符遍历，与其他字符串依次比较对应位置上的字符，并记录查找位置，如果找到不相等或者对应字符串的长度到了限制，就找到了。

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if (i < len(strs[j]) and ch != strs[j][i]) or i == len(strs[j]):
                    return strs[0][:i]
        
        return strs[0]

# @lc code=end

