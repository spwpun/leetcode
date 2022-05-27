#
# @lc app=leetcode.cn id=699 lang=python3
#
# [699] 掉落的方块
#
# 思路：

# from typing import List

# @lc code=start
# 1. 暴力枚举，自己写了一半，调样例调不下去了
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        res = []
        max_heights = [0]*len(positions)
        for i in range(len(positions)):
            x, y = positions[i]
            if i == 0:
                max_heights[i] = y
            for j in range(i):
                left, height = positions[j]
                right = left + height
                # 如果两个方块重叠，则更新最大高度
                if max(x, left) < min(x+y, right):
                    max_heights[i] = max(max_heights[i], max_heights[j]+y)
                elif j == i - 1 and max_heights[i] == 0:
                    max_heights[i] = y
            max_height = max(max_heights)
            res.append(max_height)
            # print(max_heights)
        return res

# 2. 线段树方法，有模板，第一次接触，
# 线段树（Segment Tree）是一种二叉树形数据结构，1977 年由 Jon Louis Bentley 发明，用以存储区间或线段，并且允许快速查询结构内包含某一点的所有区间。
# 一个包含 nn 个区间的线段树，空间复杂度为 O(n)O(n)，查询的时间复杂度则为 O(log\ n+k)O(log n+k)，其中 kk 是符合条件的区间数量。
class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = 0

class SegmentTree:
    def __init__(self):
        self.root = Node()
    
    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: int) -> None:
        if l <= lc and rc <= r:
            node.add = v
            node.val = v
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)
 
    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> int:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, 0
        if l <= mid:
            ans = SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = max(ans, SegmentTree.query(node.rs, mid + 1, rc, l, r))
        return ans
    
    @staticmethod
    def pushdown(node: Node) -> None:
        # 懒标记, 在需要的时候才开拓节点和赋值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.add, node.rs.add, node.ls.val, node.rs.val = [node.add] * 4
        node.add = 0
    
    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为最大值
        node.val = max(node.ls.val, node.rs.val)

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans, st, max_range = [], SegmentTree(), int(1e9)
        for a, length in positions:
            SegmentTree.update(st.root, 0, max_range, a, a + length - 1, SegmentTree.query(st.root, 0, max_range, a, a + length - 1) + length)
            ans.append(st.root.val)
        return ans

# input = [[50,47],[95,48],[88,77],[84,3],[53,87],[98,79],[88,28],[13,22],[53,73],[85,55]]
# s = Solution()
# print(s.fallingSquares(input))
# @lc code=end

