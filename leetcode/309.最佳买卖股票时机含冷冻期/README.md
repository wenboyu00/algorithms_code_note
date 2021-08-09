# 题目
<p>给定一个整数数组，其中第<em>&nbsp;i</em>&nbsp;个元素代表了第&nbsp;<em>i</em>&nbsp;天的股票价格 。​</p>

<p>设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:</p>

<ul>
	<li>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</li>
	<li>卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。</li>
</ul>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,2,3,0,2]
<strong>输出: </strong>3 
<strong>解释:</strong> 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]</pre>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div>

# Python

```python
"""
在122题的基础上增加了冷静期
因为k是正无穷，所以取消k状态
因为增加冷冻期：卖出后 等1天 才能交易
所以状态转移方程改为：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) 
dp[i][1] = max(dp[i-1][1], dp[i-2][1] - prices[i]) 
第i天要购买的时候，要从 i-2 的状态，跳过一天
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
```

# Go

```go
func maxProfit(prices []int) int {
   n := len(prices)
   dpi0 := 0
   dpi1 := math.MinInt32
   dpPre0 :=0
   for i := 0; i < n; i++ {
      temp := dpi0
      dpi0 = max(dpi0, dpi1+prices[i])
      dpi1 = max(dpi1, dpPre0-prices[i])
      dpPre0 = temp
   }
   return dpi0
}
```