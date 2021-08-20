# 题目
<p>给定一个二叉树，判断其是否是一个有效的二叉搜索树。</p>

<p>假设一个二叉搜索树具有如下特征：</p>

<ul>
	<li>节点的左子树只包含<strong>小于</strong>当前节点的数。</li>
	<li>节点的右子树只包含<strong>大于</strong>当前节点的数。</li>
	<li>所有左子树和右子树自身必须也是二叉搜索树。</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong>
    2
   / \
  1   3
<strong>输出:</strong> true
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:
</strong>    5
   / \
  1   4
&nbsp;    / \
&nbsp;   3   6
<strong>输出:</strong> false
<strong>解释:</strong> 输入为: [5,1,4,null,null,3,6]。
&nbsp;    根节点的值为 5 ，但是其右子节点值为 4 。
</pre>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉搜索树</li><li>二叉树</li></div></div>
# 分析
不能说和面试今典04.05有相似，简直一模一样

# Python

```python
class Solution:
    # bst 中序 从小到大，所有左子树小于根节点，所有右子树大于节点
    def isValidBST(self, root: TreeNode) -> bool:

        def is_valid_bst(root: TreeNode, min_val: int, max_val: int) -> bool:
            if root is None:
                return True
            if min_val < root.val < max_val:
                return is_valid_bst(root.left, min_val, root.val) and \
                       is_valid_bst(root.right, root.val, max_val)
            else:
                return False

        return is_valid_bst(root, float("-INF"), float("INF"))
```

# Go

```go
func isValidBST(root *TreeNode) bool {
   var isValid func(root *TreeNode, min int, max int) bool
   isValid = func(root *TreeNode, min int, max int) bool {
      if root == nil {
         return true
      }
      if min < root.Val && max > root.Val {
         return isValid(root.Left, min, root.Val) &&
            isValid(root.Right, root.Val, max)
      } else {
         return false
      }
   }
   return isValid(root, math.MinInt64, math.MaxInt64)
}
```
