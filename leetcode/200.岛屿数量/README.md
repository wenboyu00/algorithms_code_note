# 题目
<p>给你一个由 <code>'1'</code>（陆地）和 <code>'0'</code>（水）组成的的二维网格，请你计算网格中岛屿的数量。</p>

<p>岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。</p>

<p>此外，你可以假设该网格的四条边均被水包围。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 300</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>
<div><div>Related Topics</div><div><li>深度优先搜索</li><li>广度优先搜索</li><li>并查集</li><li>数组</li><li>矩阵</li></div></div>



# Python

```python
class Solution:
    """
    深度优先算法和79题单词搜索类似
    先遍历
    找到1
    - 进入深度优先递归，每次递归
     - 判断越界和已经浏览过
     - 把当前位置加入已经浏览
     - 对当前位置上下左右递归
    - 岛屿数量+1
        因为只要出现1就表示有一个岛屿，用递归把岛屿面积走出来即可
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = []
        for _ in range(m):
            visited.append([False] * n)

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count
```

# Go

```go
func numIslands(grid [][]byte) int {
   m := len(grid)
   n := len(grid[0])
   count := 0
   visited := make([][]bool, m)
   for i := 0; i < m; i++ {
      visited[i] = make([]bool, n)
   }

   var dfs func(i int, j int)
   dfs = func(i int, j int) {
      if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == '0' {
         return
      }
      if visited[i][j] {
         return
      }
      visited[i][j] = true
      dfs(i+1, j)
      dfs(i-1, j)
      dfs(i, j+1)
      dfs(i, j-1)
   }
   for row := 0; row < m; row++ {
      for col := 0; col < n; col++ {
         if grid[row][col] == '1' && visited[row][col] != true {
            dfs(row, col)
            count += 1
         }
      }
   }
   return count
}
```