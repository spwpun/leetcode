n = int(input())
nums = list(map(int, input().split()))
print(n, nums)

nums.sort(reverse=True)
nums = nums[:3]
print(nums)
for i in range(3):
    nums[i] = str(nums[i])
nums.sort(reverse=True)
print(''.join(nums))