# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        if head is None:
            return None
        pre = None
        next_ = None
        while True:
            next_ = head.next
            head.next = pre
            pre = head
            if next_ is None:
                break
            head = next_
        return pre