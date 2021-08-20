# 题目
<p>给定一个二叉搜索树的根节点 <code>root</code> ，和一个整数 <code>k</code> ，请你设计一个算法查找其中第 <code>k</code><strong> </strong>个最小元素（从 1 开始计数）。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;" />
<pre>
<strong>输入：</strong>root = [3,1,4,null,2], k = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [5,3,6,2,4,null,null,1], k = 3
<strong>输出：</strong>3
</pre>

<p> </p>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数为 <code>n</code> 。</li>
	<li><code>1 <= k <= n <= 10<sup>4</sup></code></li>
	<li><code>0 <= Node.val <= 10<sup>4</sup></code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 <code>k</code> 小的值，你将如何优化算法？</p>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉搜索树</li><li>二叉树</li></div></div>

# Python

```python
class Solution:
    """
    根据BST的特性，左小右大，子树依然，使用中序遍历找到第k个数
    """

    def __init__(self):
        self.res = 0
        # 排名
        self.rank = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if root is None:
            return root
        self.traverse(root, k)
        self.rank += 1
        if k == self.rank:
            self.res = root.val
        self.traverse(root, k)
```

# Go

```go
func kthSmallest(root *TreeNode, k int) int {
   res := 0
   rank := 0

   var reverse func(root *TreeNode, k int)

   reverse = func(root *TreeNode, k int) {
      if root == nil {
         return
      }
      reverse(root.Left, k)
      rank += 1
      if rank == k {
         res = root.Val
      }
      reverse(root.Right, k)
   }
   reverse(root, k)
   return res
}
```