# 题目
<p>给定一个 <code>m x n</code> 二维字符网格 <code>board</code> 和一个字符串单词 <code>word</code> 。如果 <code>word</code> 存在于网格中，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>输入：</strong>board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 <= m, n <= 6</code></li>
	<li><code>1 <= word.length <= 15</code></li>
	<li><code>board</code> 和 <code>word</code> 仅由大小写英文字母组成</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以使用搜索剪枝的技术来优化解决方案，使其在 <code>board</code> 更大的情况下可以更快解决问题？</p>
<div><div>Related Topics</div><div><li>数组</li><li>回溯</li><li>矩阵</li></div></div>

# Python

```python
def exist(self, board: List[List[str]], word: str) -> bool:
    """
    回溯算法-dfs
    先找到和第一个字母相同的位置 开始回溯找
    """

    m = len(board)
    n = len(board[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # 找到和字母第一位相同的位置开始回溯
            if word[0] == board[i][j]:
                if self.backtrack(board, i, j, word, 0, visited):
                    return True
    return False

def backtrack(self, board, row, col, word, idx, visited):
    """
    回溯算法,如果此格子上的值和word[idx]相等就接着回溯找下一个
    board:二维网格
    row：行值
    col:列值
    word:需要找到的字符串
    idx:需要找到字符的索引
    visited:标记是否已经访问，避免重复

    结束条件：回溯长度和word长度相等
    """
    # 结束条件
    if idx == len(word):
        return True
    # 处理越界情况
    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
        return False
    # 已经访问过
    if visited[row][col]:
        return False
    # 是否相等，不相等就返回
    if board[row][col] != word[idx]:
        return False
    # 回溯，加入列表中
    visited[row][col] = True
    # 从格子的上下左右寻找(回溯)
    if self.backtrack(board, row + 1, col, word, idx + 1, visited) or \
            self.backtrack(board, row - 1, col, word, idx + 1, visited) or \
            self.backtrack(board, row, col + 1, word, idx + 1, visited) or \
            self.backtrack(board, row, col - 1, word, idx + 1, visited):
        return True
    # 撤销选择
    visited[row][col] = False
    return False
```

# Go

```go
func exist(board [][]byte, word string) bool {
   //先找到和第一个字母相同的格子，然后回溯寻找剩下的
   m := len(board)
   n := len(board[0])
   wordLen := len(word)
   visited := make([][]bool, m)

   for i := 0; i < m; i++ {
      visited[i] = make([]bool, n)
   }

   var backtrack func(row int, col int, idx int) bool
   backtrack = func(row int, col int, idx int) bool {
      // 结束条件：字符索引到字符串尾部
      if idx == wordLen {
         return true
      }
      if row < 0 || col < 0 || row >= m || col >= n {
         return false
      }
      if visited[row][col] {
         return false
      }
      if board[row][col] != word[idx] {
         return false
      }
      // 添加选择
      visited[row][col] = true
      // 从格子的上下左右寻找和下一个字符 是否相等的结果
      if backtrack(row+1, col, idx+1) ||
         backtrack(row-1, col, idx+1) ||
         backtrack(row, col+1, idx+1) ||
         backtrack(row, col-1, idx+1) {
         return true
      }
      // 删除选择
      visited[row][col] = false
      return false
   }

   for i := 0; i < n; i++ {
      for j := 0; j < n; j++ {
         if word[0] == board[i][j] {
            if backtrack(i, j, 0) {
               return true
            }
         }
      }
   }
   return false
}
```