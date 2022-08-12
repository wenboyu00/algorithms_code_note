# 题目
<p>一个机器人位于一个 <code>m x n</code><em> </em>网格的左上角 （起始点在下图中标记为 “Start” ）。</p>

<p>机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。</p>

<p>问总共有多少条不同的路径？</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" />
<pre>
<strong>输入：</strong>m = 3, n = 7
<strong>输出：</strong>28</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>m = 3, n = 2
<strong>输出：</strong>3
<strong>解释：</strong>
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>m = 7, n = 3
<strong>输出：</strong>28
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>m = 3, n = 3
<strong>输出：</strong>6</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= m, n <= 100</code></li>
	<li>题目数据保证答案小于等于 <code>2 * 10<sup>9</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>数学</li><li>动态规划</li><li>组合数学</li></div></div>

# Python

```python
def uniquePaths(self, m: int, n: int) -> int:
    """
    m是行，n是列
    动态规划
    base case:
        第一排or第一列的网格只能向右或向下，因此路径数都是1
        第一列 只有向下一种走法,初始化为 1
        第一行 只有向右一种走法,初始化为 1
    dp数组:
       dp[i][j] 到达i,j坐标的路径和
    动态转移方程:
       dp[i][j] = dp[i-1][j]+dp[i][j-1]
       每次移动向右或向下，因此每格移动路径数等于i-1,j和i,j-1的路径数之和
    """
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
```

# Go

```go
func uniquePaths(m int, n int) int {
   dp := make([][]int, m)
   // base case
   // 第一列 只有向下一种走法,初始化为 1
   for i := 0; i < m; i++ {
      dp[i] = make([]int, n)
      dp[i][0] = 1
   }
   // 第一行 只有向右一种走法,初始化为 1
   for j := 0; j < n; j++ {
      dp[0][j] = 1
   }
   // 动态转移方程
   // 达到i,j的路径数 = i-1,j(上一个格子) + i,j-1(左一个格子)
   for i := 1; i < m; i++ {
      for j := 1; j < n; j++ {
         dp[i][j] = dp[i-1][j] + dp[i][j-1]
      }
   }
   return dp[m-1][n-1]
}
```