#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 已知头和脚的数量，计算鸡和兔子的数量
# @param headAndFoot string字符串 头和脚的数量，逗号分割
# @return string字符串
#

class Solution:
    def doCalc(self , headAndFoot: str) -> str:
        # write code here
        res = ""
        if "," not in headAndFoot:
            return "INPUTERROR"
        m, n = map(str, headAndFoot.split(","))
        if not m.isdigit() or not n.isdigit():
            return "INPUTERROR"
        m = int(m)
        n = int(n)
        x = (4*m - n) / 2
        y = m - x
        if x % 1 != 0 or y % 1 != 0:
            return "NODATA"
        elif x == 0.0 or y == 0.0:
            return "NODATA"
        else:
            x = int(x)
            y = int(y)
            res = str(x) + "," + str(y)
        
        return res

# test
s = Solution()
print(s.doCalc("2,6"))