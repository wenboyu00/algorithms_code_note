from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float("-INF")
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0


if __name__ == '__main__':
    p = [1, 3, 2, 8, 4, 9]
    f = 2
    result = Solution().maxProfit(p, f)
    print(result)
