'''
Tag: 动态规划，和HJ52 类似，只不过转移方程不一样
'''

ap, pan = map(int, input().split())
ap += 1
pan += 1
dp = [[0 for _ in range(pan)] for _ in range(ap)]
for j in range(pan):
    dp[1][j] = 1
    dp[0][j] = 1
for i in range(ap):
    dp[i][1] = 1

for i in range(2, ap):
    for j in range(2, pan):
        if i < j:
            dp[i][j] = dp[i][i]
        else:
            dp[i][j] = dp[i-j][j] + dp[i][j - 1]
print(dp[i][j])