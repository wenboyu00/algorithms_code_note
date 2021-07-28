# 题目

<p>给定一个二叉树，找出其最小深度。</p>

<p>最小深度是从根节点到最近叶子节点的最短路径上的节点数量。</p>

<p><strong>说明：</strong>叶子节点是指没有子节点的节点。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg" style="width: 432px; height: 302px;" />
<pre>
<strong>输入：</strong>root = [3,9,20,null,null,15,7]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [2,null,3,null,4,null,5,null,6]
<strong>输出：</strong>5
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数的范围在 <code>[0, 10<sup>5</sup>]</code> 内</li>
	<li><code>-1000 <= Node.val <= 1000</code></li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>广度优先搜索</li><li>二叉树</li></div></div>\n<div><li>👍 554</li><li>👎 0</li></div>

# Python

```python
def minDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    q = list()
    q.append(root)
    depth = 1
    while len(q) != 0:
        for i in range(len(q)):
            cur = q.pop(0)
            if cur.left is None and cur.right is None:
                return depth
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        depth += 1
```

# GO

```go
/*
明确起点和终点
-起点    root 根节点
-终点    叶子节点（两个子节点都为空的节点）
根据框架修改解法
 */
func minDepth(root *TreeNode) int {
   if root == nil {
      return 0
   }
   // 队列
   q := make([]TreeNode, 0)
   // 初始化起点，初始化层数（root也算一层）
   q = append(q, *root)
   depth := 1
   // 不空时循环
   for len(q) != 0 {
      // 循环一层的节点，此时队列中保存一层的节点数量，通过数量来控制。
      size := len(q)
      for i := 0; i < size; i++ {
         // 获得队首节点和实现队列pop效果
         cur := q[0]
         q = q[1:]
         // 判断是否终点
         if cur.Left == nil && cur.Right == nil {
            return depth
         }
         // 讲cur相邻的节点加入队列
         if cur.Left != nil {
            q = append(q, *cur.Left)
         }
         if cur.Right != nil {
            q = append(q, *cur.Right)

         }
      }
      // 增加层数
      depth += 1
   }
   return depth
}
```