# 题目
<p>给定正整数 <em>n</em>，找到若干个完全平方数（比如 <code>1, 4, 9, 16, ...</code>）使得它们的和等于<em> n</em>。你需要让组成和的完全平方数的个数最少。</p>

<p>给你一个整数 <code>n</code> ，返回和为 <code>n</code> 的完全平方数的 <strong>最少数量</strong> 。</p>

<p><strong>完全平方数</strong> 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，<code>1</code>、<code>4</code>、<code>9</code> 和 <code>16</code> 都是完全平方数，而 <code>3</code> 和 <code>11</code> 不是。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = <code>12</code>
<strong>输出：</strong>3 
<strong>解释：</strong><code>12 = 4 + 4 + 4</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = <code>13</code>
<strong>输出：</strong>2
<strong>解释：</strong><code>13 = 4 + 9</code></pre>
 

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 10<sup>4</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>广度优先搜索</li><li>数学</li><li>动态规划</li></div></div>

# Python

```python
def numSquares(self, n: int) -> int:
    """
    动态规划-类似硬币问题
    从固定的数组里面选数，凑一个值
     - 完全平方数，就是j平方
    base case
    - dp[i]= i 是最坏结果，即i个1相加，凑出当前值
    动态转移方程:
    - dp[i]= min(dp[i], dp[i - j*j]+1)
    - min(当前最坏情况, i-j^2的情况再+1)
        - 加1是加上最小的完全平方数
    """
    dp = [0]
    for i in range(1, n + 1):
        j = 1
        dp.append(i)
        while i - j * j >= 0:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]
```



# Go

```go
func numSquares(n int) int {
   dp := make([]int, n+1)
   for i := 1; i < n+1; i++ {
      dp[i] = i
      for j := 1; i-j*j >= 0; j++ {
         num := i - j*j
         if dp[i] > dp[num]+1 {
            dp[i] = dp[num] + 1
         }
      }
   }
   return dp[n]
}
```