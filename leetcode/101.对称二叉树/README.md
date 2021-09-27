# 题目
<p>给定一个二叉树，检查它是否是镜像对称的。</p>

<p>&nbsp;</p>

<p>例如，二叉树&nbsp;<code>[1,2,2,3,4,4,3]</code> 是对称的。</p>

<pre>    1
   / \
  2   2
 / \ / \
3  4 4  3
</pre>

<p>&nbsp;</p>

<p>但是下面这个&nbsp;<code>[1,2,2,null,3,null,3]</code> 则不是镜像对称的:</p>

<pre>    1
   / \
  2   2
   \   \
   3    3
</pre>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你可以运用递归和迭代两种方法解决这个问题吗？</p>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉树</li></div></div>

# Python

```python
def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return root
    return self.is_mirror(root.left, root.right)

def is_mirror(self, left, right) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)
```

# Go

```go
func isSymmetric(root *TreeNode) bool {
   return isMirror(root.Left, root.Right)
}

func isMirror(left *TreeNode, right *TreeNode) bool {
   if left == nil && right == nil {
      return true
   }
   if left == nil || right == nil {
      return false
   }
   if left.Val != right.Val {
      return false
   }
   return isMirror(left.Left, right.Right) && isMirror(left.Right, right.Left)
```