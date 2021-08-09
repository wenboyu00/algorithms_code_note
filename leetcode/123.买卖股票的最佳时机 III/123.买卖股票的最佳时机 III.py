from typing import List

"""
k = 2 套用框架，设置k最高2，从大到小穷举到
初始化base_case dp矩阵
把原有dp[-1][k][0] = 0 ，赋值给所有的dp[i][k][0]
把原有dp[-1][k][1] = -prices[i] ，赋值给所有的dp[i][k][1]
特殊情况处理：
遇到 i=0时，直接[i][k][1] = 0，[i][k][1] = - prices[i],因为初始化已经赋值所以直接continue
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化dp矩阵，用base case值赋值默认值
        dp = []
        n = len(prices)
        for i in range(n):
            k_list = []
            # 方便k的穷举到2,所以range(3)
            for j in range(3):
                k_list.append([0, float('-INF')])
            dp.append(k_list)

        for i in range(n):
            # 穷举k, 从大到小[2,1]
            for k in range(2, 0, -1):
                if i == 0:
                    continue
                # 状态转移方程
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][2][0]


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    result = Solution().maxProfit(prices)
    print(result)
