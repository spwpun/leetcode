#
# @lc app=leetcode.cn id=675 lang=python3
#
# [675] 为高尔夫比赛砍树
#

# from collections import deque
# from typing import List

# @lc code=start
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # bfs algrithom
        def bfs(s_x, s_y, t_x, t_y, forest):
            queue = deque()
            queue.append((s_x, s_y, 0))
            visited = set()
            visited.add((s_x, s_y))
            while queue:
                x, y, step = queue.popleft()
                if x == t_x and y == t_y:
                    return step
                for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= i < len(forest) and 0 <= j < len(forest[0]) and (i, j) not in visited and forest[i][j] > 0:
                        queue.append((i, j, step + 1))
                        visited.add((i, j))
            return -1
        
        # sort the trees by their height
        trees = sorted([(i, j, forest[i][j]) for i in range(len(forest)) for j in range(len(forest[0])) if forest[i][j] > 1], key=lambda x: x[2])
        # print("trees: {}".format(trees))
        ans = preI = preJ = 0
        for i, j, h in trees:
            # if i == preI and j == preJ:
            #     continue
            # print("SourceNode: {}, {}; DstNode: {}, {}".format(preI, preJ, i, j))
            step = bfs(preI, preJ, i, j, forest)
            # print("step: {}".format(step))
            if step == -1:
                return -1
            ans += step
            preI, preJ = i, j
        
        return ans

# test on local
# if __name__ == '__main__':
#     forest = [[4,2,3],[0,0,1],[7,6,5]]
#     print(Solution().cutOffTree(forest))

# @lc code=end
