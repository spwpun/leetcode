'''
Tag:公共子串计算， 动态规划
最长公共子串是： dp[i][j] -- 表示以str1[i]和str2[j]为结尾的最长公共子串 当str1[i] == str2[j]时，dp[i][j] = dp[i-1][j-1] + 1; 否则，dp[i][j] = 0;
最优解为max(dp[i][j]),其中0<=i<len1, 0<=j<len2;

最长公共子序列是：
dp[i][j] -- 表示子串str1[0...i]和子串str[0...j]的最长公共子序列
当str1[i] == str2[j]时，dp[i][j] = dp[i-1][j-1] + 1;
否则，dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
最优解为dp[len1-1][len2-1];

'''
def common_substring(str1, str2):
    
    m = len(str1) + 1
    n = len(str2) + 1

    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if str1[i - 1] == str2[j -1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0

    res = 0
    for l in dp:
        if max(l) > res:
            res = max(l)
    return res

str1 = input()
str2 = input()
print(common_substring(str1, str2))