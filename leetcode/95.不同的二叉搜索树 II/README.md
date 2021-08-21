# 题目
<p>给你一个整数 <code>n</code> ，请你生成并返回所有由 <code>n</code> 个节点组成且节点值从 <code>1</code> 到 <code>n</code> 互不相同的不同 <strong>二叉搜索树</strong><em> </em>。可以按 <strong>任意顺序</strong> 返回答案。</p>

<p> </p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[[1]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 8</code></li>
</ul>
</div>
</div>

<div><div>Related Topics</div><div><li>树</li><li>二叉搜索树</li><li>动态规划</li><li>回溯</li><li>二叉树</li></div></div>

# Python

```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.generate(1, n)

    def generate(self, low, high) -> List[TreeNode]:
        res = []
        if low > high:
            res.append(None)
            return res
        for i in range(low, high + 1):
            # 递归构造左右子树
            left = self.generate(low, i - 1)
            right = self.generate(i + 1, high)
            # 给root节点穷举所有左右子树
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
```

# Go

```go
func generateTrees(n int) []*TreeNode {
   if n == 0 {
      return []*TreeNode{}
   }
   return generate(1, n)
}
func generate(low int, high int) []*TreeNode {
   res := []*TreeNode{}
   // base case 无区间时，返回nil节点
   if low > high {
      res = append(res, nil)
      return res
   }
   for i := low; i <= high; i++ {
      // 递归构建左右子树
      left := generate(low, i-1)
      right := generate(i+1, high)
      // 给root节点穷举所有左右子树
      for _, l := range left {
         for _, r := range right {
            root := &TreeNode{Val: i}
            root.Left = l
            root.Right = r
            res = append(res, root)
         }
      }
   }
   return res
}
```

