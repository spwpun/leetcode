'''
DFS遍历，岛问题
'''

class Solution:
    def explore(self, i, j, grid, visited):
        # explore in the grid
        print("current:", i, j)
        if (i,j) in visited:
            return 0
        elif grid[i][j] == '1':
            visited.append((i,j))
        else:
            return 0
        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if m < 0 or m == len(grid) or n < 0 or n == len(grid[0]):
                continue
            else:
                self.explore(m,n,grid,visited)
        return 1
    
    def numIslands(self , grid ):
        # write code here
        visited = []
        res = 0
        m = len(grid)  # m行
        n = len(grid[0]) # n列
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                elif grid[i][j] == '1':
                    tmp = self.explore(i,j,grid,visited)
                    print("tmp:", tmp)
                    print("visited:", visited)
                    if tmp:
                        res +=1
        return res

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
print(s.numIslands(grid))