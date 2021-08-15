# 题目
<p>翻转一棵二叉树。</p>

<p><strong>示例：</strong></p>

<p>输入：</p>

<pre>     4
   /   \
  2     7
 / \   / \
1   3 6   9</pre>

<p>输出：</p>

<pre>     4
   /   \
  7     2
 / \   / \
9   6 3   1</pre>

<p><strong>备注:</strong><br>
这个问题是受到 <a href="https://twitter.com/mxcl" target="_blank">Max Howell </a>的 <a href="https://twitter.com/mxcl/status/608682016205344768" target="_blank">原问题</a> 启发的 ：</p>

<blockquote>谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。</blockquote>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉树</li></div></div>

# Python

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

# Go

```go
func invertTree(root *TreeNode) *TreeNode {
   // base case
   if root == nil{
      return nil
   }
   // 前序遍历
   // root节点的左右节点交换
   temp := root.Left
   root.Left = root.Right
   root.Right = temp
   // 让左右子节点继续翻转它们的子节点
   invertTree(root.Left)
   invertTree(root.Right)
   return root
}
```