# 题目
<p>给定一个整数数组 <code>prices</code> ，它的第<em> </em><code>i</code> 个元素 <code>prices[i]</code> 是一支给定的股票在第 <code>i</code><em> </em>天的价格。</p>

<p>设计一个算法来计算你所能获取的最大利润。你最多可以完成 <strong>k</strong> 笔交易。</p>

<p><strong>注意：</strong>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>k = 2, prices = [2,4,1]
<strong>输出：</strong>2
<strong>解释：</strong>在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 2, prices = [3,2,6,5,0,3]
<strong>输出：</strong>7
<strong>解释：</strong>在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= k <= 100</code></li>
	<li><code>0 <= prices.length <= 1000</code></li>
	<li><code>0 <= prices[i] <= 1000</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li></div></div>

# Python

```python
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
```

# Go

```python
func maxProfit(k int, prices []int) int {
   n := len(prices)
   if n == 0 {
      return 0
   }
   if k > n/2 {
      k = n / 2
   }
   dp := make([][][]int, n)
   for i := 0; i < n; i++ {
      kList := make([][]int, k+1)
      for j := 0; j < k+1; j++ {
         kList[j] = []int{0, -prices[i]}
      }
      dp[i] = kList
   }
   for i := 0; i < n; i++ {
      for j := k; j > 0; j-- {
         if i == 0 {
            continue
         }
         dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
         dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
      }
   }
   return dp[n-1][k][0]
}
```