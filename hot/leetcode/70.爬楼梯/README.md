# 题目

<p>假设你正在爬楼梯。需要 <em>n</em>&nbsp;阶你才能到达楼顶。</p>

<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>

<p><strong>注意：</strong>给定 <em>n</em> 是一个正整数。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> 2
<strong>输出：</strong> 2
<strong>解释：</strong> 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> 3
<strong>输出：</strong> 3
<strong>解释：</strong> 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
</pre>

# Python

```python
"""
0层台阶： 1种
1层台阶: 1种
2层台阶: [2, 1+1] 2种
3层台阶：
    先走1层 3-1 = 2层台阶
    先走2层 3-2 = 1层台阶
    dp[3] = dp[3-1] + dp[3-2]
把走n层的需要几种种方法问题推到
    先走1层台阶的方法数和先走2层台阶的方法数
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始化把dp数组存储结果
        dp = [0] * (n + 1)
        # base case
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            # n阶 = n-1阶 + n-2阶
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
```

Go

```go
package main

func climbStairs(n int) int {
   dp := make([]int, n+1)
   dp[0] = 1
   dp[1] = 1
   for i := 2; i <= n; i++ {
      dp[i] = dp[i-1] + dp[i-2]
   }
   return dp[n]
}
```