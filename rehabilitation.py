# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# 康复训练，求最小的花费
# A: list, 接下来N天，第K所需的花费为A[K]
# X: int, 需要X次session
# Y: int, 每次session需要间隔Y天

def solution(A, X, Y):
    # write your code in Python (Python 3.6)
    # 从第i天开始所需的花费，dp[i]
    n_days = len(A)
    dp = []
    for i in range(len(A)):
        if (i + (X - 1)*Y) >= n_days:
            break
        else:
            sum_cost = 0
            for j in range(X):
                sum_cost += A[i + j*Y]
            dp.append(sum_cost)
    return min(dp)

# Test
A = [4, 2, 5, 4, 3, 5, 1, 4, 2, 7]
X = 3
Y = 2
print(solution(A, X, Y))