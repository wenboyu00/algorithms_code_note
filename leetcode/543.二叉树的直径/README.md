# 题目
<p>给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。</p>

<p>&nbsp;</p>

<p><strong>示例 :</strong><br>
给定二叉树</p>

<pre>          1
         / \
        2   3
       / \     
      4   5    
</pre>

<p>返回&nbsp;<strong>3</strong>, 它的长度是路径 [4,2,1,3] 或者&nbsp;[5,2,1,3]。</p>

<p>&nbsp;</p>

<p><strong>注意：</strong>两结点之间的路径长度是以它们之间边的数目表示。</p>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉树</li></div></div>

# Python

```python
def diameterOfBinaryTree(self, root: TreeNode) -> int:
    """
    二叉树的直径：从一个节点到另一个节点最长的路径
    题目求：任意节点，所以要每次递归是都判断当前的路径是否是最大
    """

    def deep(root):
        if root is None:
            return 0
        left = deep(root.left)
        right = deep(root.right)
        # 判断此节点路径是否是最长
        self.ans = max(self.ans, left + right + 1)
        # 返回左右路径中最长+1
        return max(left, right)

    deep(root)
    return self.ans
```

# Go

```go
func diameterOfBinaryTree(root *TreeNode) int {
   ans := 0
   var depth func(root *TreeNode) int
   depth = func(root *TreeNode) int {
      if root == nil {
         return 0
      }
      left := depth(root.Left)
      right := depth(root.Right)
      if left+right > ans {
         ans = left + right
      }
      if left > right {
         return left + 1
      } else {
         return right + 1
      }
   }
   depth(root)
   return ans
}
```