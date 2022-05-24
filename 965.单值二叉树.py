#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#
# 思路：dfs遍历二叉树，如果遍历到的节点的值与当前节点的值不同，则返回False，如果node为空，则返回True

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # DFS
        def dfs(node):
            if not node:
                return True
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)
# @lc code=end

