# 题目
<p>给定一个数组，它的第<em> </em><code>i</code> 个元素是一支给定的股票在第 <code>i</code><em> </em>天的价格。</p>

<p>设计一个算法来计算你所能获取的最大利润。你最多可以完成 <strong>两笔 </strong>交易。</p>

<p><strong>注意：</strong>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>prices = [3,3,5,0,0,3,1,4]
<strong>输出：</strong>6
<strong>解释：</strong>在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [1,2,3,4,5]
<strong>输出：</strong>4
<strong>解释：</strong>在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>prices = [7,6,4,3,1] 
<strong>输出：</strong>0 
<strong>解释：</strong>在这个情况下, 没有交易完成, 所以最大利润为 0。</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>prices = [1]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= prices.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= prices[i] <= 10<sup>5</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div>

# Python

```python
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
```

# Go

```python
func maxProfit(prices []int) int {
   n := len(prices)
   // 初始化 dp数组，用base case作为默认值
   dp := make([][][]int, 0)
   for i := 0; i < n; i++ {
      kk := make([][]int, 0)
      for k := 0; k < 3; k++ {
         kk = append(kk, []int{0, -prices[i]})
      }
      dp = append(dp, kk)
   }
   for i := 0; i < n; i++ {
      for k := 2; k > 0; k-- {
         if i == 0 {
            continue
         }
         dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
         dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])

      }

   }
   return dp[n-1][2][0]
}
```