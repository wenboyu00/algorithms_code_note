class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        m是行，n是列
        动态规划
        base case:
            第一排or第一列的网格只能向右或向下，因此路径数都是1
            第一列 只有向下一种走法,初始化为 1
            第一行 只有向右一种走法,初始化为 1
        dp数组:
           dp[i][j] 到达i,j坐标的路径和
        动态转移方程:
           dp[i][j] = dp[i-1][j]+dp[i][j-1]
           每次移动向右或向下，因此每格移动路径数等于i-1,j和i,j-1的路径数之和
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
