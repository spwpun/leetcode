'''
Tag: 动态规划，最长递增字序列
'''

def LIS(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def RIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums), -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

N = int(input())
nums = list(map(int, input().split()))
dp_l = LIS(nums)
dp_r = RIS(nums)
sum_q = []
for i in range(len(nums)):
    sum_q.append(dp_l[i] + dp_r[i] - 1)
print(N - max(sum_q))
''' Test ouput:
8
188 187 150 178 189 167 156 190
3
'''