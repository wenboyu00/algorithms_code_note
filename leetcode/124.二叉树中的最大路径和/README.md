# 题目
<p><strong>路径</strong> 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 <strong>至多出现一次</strong> 。该路径<strong> 至少包含一个 </strong>节点，且不一定经过根节点。</p>

<p><strong>路径和</strong> 是路径中各节点值的总和。</p>

<p>给你一个二叉树的根节点 <code>root</code> ，返回其 <strong>最大路径和</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;" />
<pre>
<strong>输入：</strong>root = [1,2,3]
<strong>输出：</strong>6
<strong>解释：</strong>最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" />
<pre>
<strong>输入：</strong>root = [-10,9,20,null,null,15,7]
<strong>输出：</strong>42
<strong>解释：</strong>最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目范围是 <code>[1, 3 * 10<sup>4</sup>]</code></li>
	<li><code>-1000 <= Node.val <= 1000</code></li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>动态规划</li><li>二叉树</li></div></div><br>

# Python

```python
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    self.ans = float("-inf")
    self.max_path(root)
    return self.ans

def max_path(self, root):
    """
    1. 把当前节点和左右节点中最大的作为路径的一部分，作为路径和返回
    - 从左右节点中选择路径和最大的+ 当前节点 = 新的节点和返回
    2. 更新最大路径和答案
    比较答案和当前的路径和 = 左右子数路径和+当前路径val
    """
    # base case 为空是值为0
    if root is None:
        return 0
    # 获取左右子树最大路径和
    left = max(0, self.max_path(root.left))
    right = max(0, self.max_path(root.right))
    # 更新答案
    self.ans = max(self.ans, left + root.val + right)
    # 返回当前路径和
    return root.val + max(left, right)
```

# Go

```go
func maxPathSum(root *TreeNode) int {

   ans := math.MinInt64
   var maxPath func(root *TreeNode) int
   maxPath = func(root *TreeNode) int {
      if root == nil {
         return 0
      }
      left := max(0, maxPath(root.Left))
      right := max(0, maxPath(root.Right))
      ans = max(ans, left+root.Val+right)
      return root.Val + max(left, right)
   }
   maxPath(root)
   return ans
}
```