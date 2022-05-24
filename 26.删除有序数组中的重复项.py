#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
# 思路：双指针，fast指针指向的元素如果和slow指针指向的元素相同，则fast指针向后移动，slow不变，直到fast指针指向的元素和slow指针指向的元素不同时，slow指针指向的元素被fast指针指向的元素替换，slow和fast指针都向后移动，重复上述步骤，直到fast指针指向最后一个元素，此时slow指针指向的元素即为结果。
# from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        fast = slow = 1
        while fast < len(nums):
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow #, nums

# res, nums = Solution().removeDuplicates([1,1,2])
# print(res, nums)

# @lc code=end

