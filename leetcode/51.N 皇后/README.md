# 题目

<p><strong>n 皇后问题</strong> 研究的是如何将 <code>n</code> 个皇后放置在 <code>n×n</code> 的棋盘上，并且使皇后彼此之间不能相互攻击。</p>

<p>给你一个整数 <code>n</code> ，返回所有不同的 <strong>n<em> </em>皇后问题</strong> 的解决方案。</p>

<div class="original__bRMd">
<div>
<p>每一种解法包含一个不同的 <strong>n 皇后问题</strong> 的棋子放置方案，该方案中 <code>'Q'</code> 和 <code>'.'</code> 分别代表了皇后和空位。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
<strong>解释：</strong>如上图所示，4 皇后问题存在两个不同的解法。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[["Q"]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 9</code></li>
	<li>皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。</li>
</ul>
</div>
</div>



# Go

```go
func solveNQueens(n int) [][]string {
   // 初始化结果集
   result := make([][]string, 0)
   // 初始化棋盘
   board := make([][]string, n)
   for i := range board {
      col := make([]string, n)
      for j := range col {
         col[j] = "."
      }
      board[i] = col
   }
   backTrack(&board, 0, &result)
   return result
}
func backTrack(board *[][]string, row int, result *[][]string) {
   if row == len(*board) {
      strList := make([]string, 0)
      for _, strs := range *board {
         str := strings.Join(strs, "")
         strList = append(strList, str)
      }
      *result = append(*result, strList)
      return
   }

   n := len((*board)[row])
   for col := 0; col < n; col++ {
      if !isValid(board, row, col) {
         continue
      }
      (*board)[row][col] = "Q"
      backTrack(board, row+1, result)
      (*board)[row][col] = "."
   }
}
func isValid(board *[][]string, row int, col int) bool {
   n := len(*board)
   for i := 0; i < n; i++ {
      if (*board)[i][col] == "Q" {
         return false
      }
   }
   for i, j := row-1, col+1; i > -1 && j < n; i, j = i-1, j+1 {
      if (*board)[i][j] == "Q" {
         return false
      }
   }
   for i, j := row-1, col-1; i > -1 && j > -1; i, j = i-1, j-1 {
      if (*board)[i][j] == "Q" {
         return false
      }
   }
   return true
}
```
