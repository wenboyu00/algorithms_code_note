# 题目
<p>给定一个整数数组 <code>prices</code>，其中第 <code>i</code> 个元素代表了第 <code>i</code> 天的股票价格 ；整数 <code>fee</code> 代表了交易股票的手续费用。</p>

<p>你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。</p>

<p>返回获得利润的最大值。</p>

<p><strong>注意：</strong>这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>prices = [1, 3, 2, 8, 4, 9], fee = 2
<strong>输出：</strong>8
<strong>解释：</strong>能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>prices = [1,3,7,5,10,3], fee = 3
<strong>输出：</strong>6
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= prices.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>1 <= prices[i] < 5 * 10<sup>4</sup></code></li>
	<li><code>0 <= fee < 5 * 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>贪心</li><li>数组</li><li>动态规划</li></div></div>

# Pyhon

```python
def maxProfit(self, prices: List[int], fee: int) -> int:
    n = len(prices)
    dp_i_0, dp_i_1 = 0, float("-INF")
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
        dp_i_1 = max(dp_i_1, temp - prices[i])
    return dp_i_0
```

# Go

```go
def maxProfit(self, prices: List[int], fee: int) -> int:
    n = len(prices)
    dp_i_0, dp_i_1 = 0, float("-INF")
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
        dp_i_1 = max(dp_i_1, temp - prices[i])
    return dp_i_0
```