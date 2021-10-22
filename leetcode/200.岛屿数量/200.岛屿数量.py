from typing import List


class Solution:
    """
    深度优先算法和79题单词搜索类似
    先遍历
    找到1
    - 进入深度优先递归，每次递归
     - 判断越界和已经浏览过
     - 把当前位置加入已经浏览
     - 对当前位置上下左右递归
    - 岛屿数量+1
        因为只要出现1就表示有一个岛屿，用递归把岛屿面积走出来即可
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = []
        for _ in range(m):
            visited.append([False] * n)

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))
