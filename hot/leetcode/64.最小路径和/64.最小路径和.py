from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # base case
        # dp[0][0] = grid[0][0]
        dp = []
        for i in range(m):
            dp.append([0] * n)
        dp[0][0] = grid[0][0]
        # 提前计算出dp[0][j]和dp[i][0]让i,j从1开始迭代
        # dp[i][0],每行第一个(第一列所有行),格子当前值+上一个值
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        # dp[0][j],每列第一个(第一行所有列)，格子当前值+左一个值
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                # 上一个格子和左一个格子中取最小的路径和+当前格子值
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))
