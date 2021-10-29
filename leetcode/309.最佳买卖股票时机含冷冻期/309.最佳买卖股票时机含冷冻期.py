from typing import List

"""
在122题的基础上增加了冷静期
因为k是正无穷，所以取消k状态
因为增加冷冻期：卖出后 等1天 才能交易
所以状态转移方程改为：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) 
dp[i][1] = max(dp[i-1][1], dp[i-2][1] - prices[i]) 
第i天要购买的时候，要从 i-2 的状态，跳过一天
最后改为：
dp[i][0] ==> dp_i_0,第i天未持有的利润
dp[i][1] ==> dp_i_1,第i天持有的利润
dp[i-2][- ==> dp_pre_0,第i-2天未持有的利润，包括冷静期
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0, dp_i_1 = 0, float("-INF")
        # dp[i-2][0] = 0
        dp_pre_0 = 0
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0


if __name__ == '__main__':
    p = [1, 2, 3, 0, 2]
    result = Solution().maxProfit(p)
    print(result)
