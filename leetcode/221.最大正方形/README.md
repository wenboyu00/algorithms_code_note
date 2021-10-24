# 题目
<p>在一个由 <code>'0'</code> 和 <code>'1'</code> 组成的二维矩阵内，找到只包含 <code>'1'</code> 的最大正方形，并返回其面积。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;" />
<pre>
<strong>输入：</strong>matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" style="width: 165px; height: 165px;" />
<pre>
<strong>输入：</strong>matrix = [["0","1"],["1","0"]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["0"]]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 <= m, n <= 300</code></li>
	<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>动态规划</li><li>矩阵</li></div></div>

# Python

```python
def maximalSquare(self, matrix: List[List[str]]) -> int:
    max_side = 0
    m = len(matrix)
    n = len(matrix[0])
    if m == 0 or n == 0:
        return max_side
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                # base case，给第一列和第一行dp赋值为1
                if i == 0 or j == 1:
                    dp[i][j] = 1
                else:
                    # 以dp[i][j]为右下角的最长边 = min(上，坐上，左) +1
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                # 更新最大边长变量
                max_side = max(max_side, dp[i][j])
    return max_side * max_side
```

# Go

```go
func maximalSquare(matrix [][]byte) int {
   maxSide := 0
   m := len(matrix)
   n := len(matrix[0])
   if m == 0 || n == 0 {
      return maxSide
   }
   dp := make([][]int, m)
   for i := 0; i < m; i++ {
      dp[i] = make([]int, n)
   }
   for i := 0; i < m; i++ {
      for j := 0; j < n; j++ {
         if matrix[i][j] == '1' {
            if i == 0 || j == 0 {
               dp[i][j] = 1
            } else {
               dp[i][j] = min(min(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1]) + 1
            }
            if maxSide < dp[i][j] {
               maxSide = dp[i][j]
            }
         }
      }
   }
   return maxSide * maxSide
}
```