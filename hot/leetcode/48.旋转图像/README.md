# 题目 
<p>给定一个 <em>n </em>× <em>n</em> 的二维矩阵 <code>matrix</code> 表示一个图像。请你将图像顺时针旋转 90 度。</p>

<p>你必须在<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a></strong> 旋转图像，这意味着你需要直接修改输入的二维矩阵。<strong>请不要 </strong>使用另一个矩阵来旋转图像。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" style="width: 642px; height: 242px;" />
<pre>
<strong>输入：</strong>matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>[[7,4,1],[8,5,2],[9,6,3]]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" style="width: 800px; height: 321px;" />
<pre>
<strong>输入：</strong>matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
<strong>输出：</strong>[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[1]]
<strong>输出：</strong>[[1]]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>matrix = [[1,2],[3,4]]
<strong>输出：</strong>[[3,1],[4,2]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>matrix.length == n</code></li>
	<li><code>matrix[i].length == n</code></li>
	<li><code>1 <= n <= 20</code></li>
	<li><code>-1000 <= matrix[i][j] <= 1000</code></li>
</ul>
<div><div>Related Topics</div><div><li>数组</li><li>数学</li><li>矩阵</li></div></div>

# Python 00

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1.左上-右下 对角线翻转
        2.左右 垂直线翻转
        """
        n = len(matrix)
        # 左上右下 对角线翻转
        for i in range(n):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # 左右 垂直线翻转
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
```

# Python 01

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        一圈一圈旋转赋值，用tmp做临时变量
        """
        # 一轮完成4个元素旋转，因此从左上角开始旋转到1/4处
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 保存左上角
                tmp = matrix[i][j]
                # 左下角->到左上角
                matrix[i][j] = matrix[n - 1 - j][i]
                # 右下角->左下角
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # 右上角 -> 右下角
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # 保存左上角 -> 右上角
                matrix[j][n - 1 - i] = tmp
```

# Go

```go
func rotate(matrix [][]int) {
   n := len(matrix)
   // 对角线 翻转
   for i := 0; i < n; i++ {
      for j := 0; j < i; j++ {
         tmp := matrix[i][j]
         matrix[i][j] = matrix[j][i]
         matrix[j][i] = tmp
      }
   }
   // 垂直 翻转
   for i := 0; i < n; i++ {
      for left, right := 0, n-1; left < right; left, right = left+1, right-1 {
         tmp := matrix[i][left]
         matrix[i][left] = matrix[i][right]
         matrix[i][right] = tmp
      }
   }
}
```

