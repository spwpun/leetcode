'''
Tag: 动态规划
'''

def walk_solutions(n, m):
    n += 1
    m += 1
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            if i == 1:
                dp[i][j] = j + 1
            elif j == 1:
                dp[i][j] = i + 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[i][j]

n, m = map(int, input().split())
print(walk_solutions(n, m))