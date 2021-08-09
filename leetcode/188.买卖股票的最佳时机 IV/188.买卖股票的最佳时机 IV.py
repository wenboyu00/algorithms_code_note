from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # 一次交易至少需要2天，n天只能做n/2次交易,k大于n/2也无用
        # 所以，k和n/2 取最小作为交易次数
        k = min(k, n//2)
        # 初始化dp数组
        dp = []
        for i in range(n):
            # 因为需要下标为k的数据，所以k+1才能得到
            kk = [[0, -prices[i]]] * (k+1)
            dp.append(kk)

        for i in range(n):
            for j in range(k, 0, -1):
                # 第0天情况已经赋值默认值，直接跳过
                if i == 0:
                    continue
                # 状态转移方程
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]


if __name__ == '__main__':
    prices = [2, 4, 1]
    k = 2
    result = Solution().maxProfit(k, prices)
    print(result)
