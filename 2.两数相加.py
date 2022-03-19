#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode)->ListNode:
        val_1 = self.get_value(l1)
        val_2 = self.get_value(l2)
        sum_val = val_1 + val_2

        return self.put_in_list(sum_val)

    def get_value(self, l):
        value = 0
        i = 0
        while True:
            value += l.val*10**i
            if l.next == None:
                break
            l = l.next
            i += 1
        
        return value

    def put_in_list(self, value):
        start_node = ListNode()
        prev_node = None
        curr_node = None

        value_re_str = str(value)[::-1]
        # print("[Debug]", value, value_re_str)
        for i in range(len(value_re_str)):
            if i == 0:
                start_node.val = int(value_re_str[i])
                curr_node = start_node
            else:
                curr_node = ListNode(int(value_re_str[i]))
                prev_node.next = curr_node
            prev_node = curr_node
        
        # print("[Debug]", start_node)

        return start_node

# @lc code=end

