from typing import List

"""
套用框架
# base case：
dp[-1][k][0] = dp[i][0][0] = 0 
dp[-1][k][1] = dp[i][0][1] = -infinity 
# 状态转移方程： 
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) 
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]

简化base case
因为新状态和相邻的状态有关，不需要dp数组，只需要存储相邻状态即可
所以：dp_i_0, dp_i_1 = 0, float('-INF')
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp_i_0 未持有默认 0
        # dp_i_0 持有默认 负无穷
        dp_i_0, dp_i_1 = 0, float('-INF')
        for i in range(n):
            # 今天未持有 = 昨天没有选择无操作 与 已持有卖出 取最大值
            # 已持有 = 昨天已持有误操作 与 未持有买入 取最大值
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0


if __name__ == '__main__':
    p = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(p)
    print(result)
