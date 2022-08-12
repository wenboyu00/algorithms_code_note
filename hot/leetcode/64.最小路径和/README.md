# 题目
<p>给定一个包含非负整数的 <code><em>m</em> x <em>n</em></code> 网格 <code>grid</code> ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。</p>

<p><strong>说明：</strong>每次只能向下或者向右移动一步。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>输入：</strong>grid = [[1,3,1],[1,5,1],[4,2,1]]
<strong>输出：</strong>7
<strong>解释：</strong>因为路径 1→3→1→1→1 的总和最小。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [[1,2,3],[4,5,6]]
<strong>输出：</strong>12
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 200</code></li>
	<li><code>0 <= grid[i][j] <= 100</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li><li>矩阵</li></div></div>

# Python

```python
def minPathSum(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    # base case
    # dp[0][0] = grid[0][0]
    dp = []
    for i in range(m):
        dp.append([0] * n)
    dp[0][0] = grid[0][0]
    # 提前计算出dp[0][j]和dp[i][0]让i,j从1开始迭代
    # dp[i][0],每行第一个(第一列所有行),格子当前值+上一个值
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    # dp[0][j],每列第一个(第一行所有列)，格子当前值+左一个值
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    # 状态转移
    for i in range(1, m):
        for j in range(1, n):
            # 上一个格子和左一个格子中取最小的路径和+当前格子值
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]
```

# Go

```go
func minPathSum(grid [][]int) int {
   m := len(grid)
   n := len(grid[0])
   // base case
   // 初始化dp结构
   dp := make([][]int, m)
   for i := 0; i < m; i++ {
      dp[i] = make([]int, n)
   }
   // 初始化dp数值
   dp[0][0] = grid[0][0]
   // 第一列，每个格子值 = 上个格子+当前
   for i := 1; i < m; i++ {
      dp[i][0] = dp[i-1][0] + grid[i][0]
   }
   // 第一行，每个格子 = 左个格子+当前
   for j := 1; j < n; j++ {
      dp[0][j] = dp[0][j-1] + grid[0][j]
   }
   // 状态转移
   for i := 1; i < m; i++ {
      for j := 1; j < n; j++ {
         // 当前格子和 = 上一个格子和左一个格子中取最小的路径和+当前格子值
         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
      }
   }
   return dp[m-1][n-1]
}

func min(int1 int, int2 int) int {
   if int1 > int2 {
      return int2
   } else {
      return int1
   }
}
```