#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# from typing import List

# comment below when submitting!!!!
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None and list2 == None:
            return None
        elif list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        else:
            list1_vals = self.get_list_val(list1)
            list2_vals = self.get_list_val(list2)
            list1_vals.extend(list2_vals)
            list1_vals.sort()
            
            res = self.convert2listnode(list1_vals)


            return res
    
    def get_list_val(self, l:ListNode):
        vals = []
        curr = l
        while True:
            vals.append(curr.val)
            if curr.next == None:
                break
            curr = curr.next
        
        return vals
    
    def convert2listnode(self, l:list):
        res_node = ListNode(l[0])
        prev_node = res_node
        for i in range(1, len(l)):
            curr_node = ListNode(l[i])
            prev_node.next = curr_node
            prev_node = curr_node
        
        return res_node


# @lc code=end

