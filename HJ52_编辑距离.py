'''
Tag: dp， 编辑距离
'''

def c_distance(str1, str2):
    # 矩阵长度须为 str1 + 1, str2 + 1
    x = len(str1) + 1
    y = len(str2) + 1
    dp = [[0 for i in range(y)] for j in range(x)]
#     print(dp)
    for i in range(x):
        dp[i][0] = i
    for j in range(y):
        dp[0][j] = j
    for i in range(1, x):
        for j in range(1, y):
            if str1[i - 1] != str2[j - 1]:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = dp[i - 1][j - 1]
    
#     print(dp)
    return dp[i][j]

str1 = input()
str2 = input()
lev_distance = c_distance(str1, str2)
print(lev_distance)