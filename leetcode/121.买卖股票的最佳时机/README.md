# 题目
<p>给定一个数组 <code>prices</code> ，它的第 <code>i</code> 个元素 <code>prices[i]</code> 表示一支给定股票第 <code>i</code> 天的价格。</p>

<p>你只能选择 <strong>某一天</strong> 买入这只股票，并选择在 <strong>未来的某一个不同的日子</strong> 卖出该股票。设计一个算法来计算你所能获取的最大利润。</p>

<p>返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 <code>0</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[7,1,5,3,6,4]
<strong>输出：</strong>5
<strong>解释：</strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,6,4,3,1]
<strong>输出：</strong>0
<strong>解释：</strong>在这种情况下, 没有交易完成, 所以最大利润为 0。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= prices.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= prices[i] <= 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div>

# Python

```python
"""
#套用框架
## base case：
dp[-1][k][0] = dp[i][0][0] = 0 
dp[-1][k][1] = dp[i][0][1] = -infinity 
## 状态转移方程： 
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) 
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

# 此题: k = 1
## 根据base case做简化
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
            = max(dp[i-1][1][1], -prices[i])
## 因为 k = 0的base case = 0, 所以直接简化为 -prices[i]

## 简化base case
因为发现k都是1，所以k对状态转移没有影响 简化掉k
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
```

# Go

```go
func maxProfit(prices []int) int {
   n := len(prices)
   dpi0 := 0
   dpi1 := math.MinInt32
   for i := 0; i < n; i++ {
      dpi0 = max(dpi0, dpi1+prices[i])
      dpi1 = max(dpi1, -prices[i])
   }
   return dpi0
}
```