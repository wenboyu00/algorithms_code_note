# 题目

<p>给定一棵二叉搜索树，请找出其中第 <code>k</code> 大的节点的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
&nbsp;  2
<strong>输出:</strong> 4</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
<strong>输出:</strong> 4</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li>1 ≤ k ≤ 二叉搜索树元素个数</li>
</ul>
# Python

```python
"""
bst,前序是从小到大，中序是从大到小，给遍历节点计数，count==k时，则为k大的数
"""


class Solution:
    def __init__(self):
        self.count = 0
        self.result = -1

    def kthLargest(self, root: TreeNode, k: int) -> int:

        self.traverse(root, k)
        return self.result

    def traverse(self, root, k):
        if root is None:
            return root
        self.traverse(root.right, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
        self.traverse(root.left, k)
```

# Go

```go
func kthLargest(root *TreeNode, k int) int {
   count := 0
   result := -1
   var reverse func(root *TreeNode, k int)

   reverse = func(root *TreeNode, k int) {
      if root == nil {
         return
      }
      reverse(root.Right, k)
      count += 1
      if count == k {
         result = root.Val
      }
      reverse(root.Left, k)
   }
   reverse(root, k)
   return result
}
```
