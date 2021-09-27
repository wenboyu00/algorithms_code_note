# 题目
<p>给定一个二叉树，找出其最大深度。</p>

<p>二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。</p>

<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>

<p><strong>示例：</strong><br>
给定二叉树 <code>[3,9,20,null,null,15,7]</code>，</p>

<pre>    3
   / \
  9  20
    /  \
   15   7</pre>

<p>返回它的最大深度&nbsp;3 。</p>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉树</li></div></div>

# Python

## 递归-深度优先

```python
def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

## 迭代-广度优先

```python
def maxDepth(self, root: TreeNode) -> int:
    stk = []
    depth = 0
    if root:
        stk.append((1, root))
    while stk:
        cur_depth, node = stk.pop()
        if node:
            stk.append((cur_depth + 1, node.left))
            stk.append((cur_depth + 1, node.right))
            depth = max(cur_depth, depth)
    return depth
```

# Go-递归-深度优先

```go
func maxDepth(root *TreeNode) int {
   if root == nil {
      return 0
   }
   leftDepth := maxDepth(root.Left)
   rightDepth := maxDepth(root.Right)
   nodeDepth := leftDepth
   if nodeDepth < rightDepth {
      nodeDepth = rightDepth
   }
   return nodeDepth + 1
}
```

