# 快速排序

def qsort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)

print(qsort([1,2,3,4,5,6,7,12,9,10]))