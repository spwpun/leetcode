#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        map = {"(":")", "[":"]", "{":"}"}

        if s[0] in ["}", ")", "]"]:
            return False
        for ch in s:
            if ch in ["(", "[", "{"]:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                
                left = stack.pop()
                print(map[left], ch)
                if map[left] != ch:
                    return False
                
        if len(stack) != 0:
            return False
        return True

# @lc code=end

