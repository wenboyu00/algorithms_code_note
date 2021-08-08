from typing import List

"""
状态转移方法，今日已购买，因为k是正无穷，所以去常数k = k-1
原式：dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
修改：dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
因为k值无法变化，取消k值
得：dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float("-INF")
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])

        return dp_i_0


if __name__ == '__main__':
    p = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(p)
    print(result)
