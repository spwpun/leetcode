import functools
# 动态规划，但是超时了
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        n = 10**9 + 7
        dp = [[0] * 2501 for _ in range(1001)]
        dp[0][startPos+1250] = 1
        for i in range(1, k + 1):
            for j in range(2501):
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
                if j < 2500:
                    dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= n
        return dp[k][endPos+1250]

# 记忆化递归，用到了修饰器
class Solution1:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        e = 10**9 + 7

        @functools.lru_cache(None) # 修饰器, 不加会超时
        def dfs(n, k):
            # 代表到endPos还有n的距离，还有k步可以走
            if k == 0:
                return 1 if n == 0 else 0
            if abs(n) > k:
                return 0
            left_go = dfs(n - 1, k - 1) # 向左走一步
            right_go = dfs(n + 1, k - 1) # 向右走一步
            return ((left_go + right_go) % e)
        return dfs(endPos - startPos, k)