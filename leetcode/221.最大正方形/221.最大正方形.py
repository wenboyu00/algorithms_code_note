from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side = 0
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return max_side
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    # base case，给第一列和第一行dp赋值为1
                    if i == 0 or j == 1:
                        dp[i][j] = 1
                    else:
                        # 以dp[i][j]为右下角的最长边 = min(上，坐上，左) +1
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    # 更新最大边长变量
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalSquare(matrix))
