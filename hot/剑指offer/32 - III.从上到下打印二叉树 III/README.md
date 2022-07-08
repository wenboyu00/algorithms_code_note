# 题目
<p>请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。</p>

<p>&nbsp;</p>

<p>例如:<br>
给定二叉树:&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回其层次遍历结果：</p>

<pre>[
  [3],
  [20,9],
  [15,7]
]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>节点总数 &lt;= 1000</code></li>
</ol>
# Python

```python
"""
奇数正序，偶数倒序
每次外层循环，设置临时数组存放，在循环结束是判断层级奇偶来决定临时数组的结果倒序还是正序
"""


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result, current, level = [], [root], 1
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level % 2:
                result.append(vals)
            else:
                result.append(vals[::-1])
            current = next_level
            level += 1
        return result
```

# Go

```go
func levelOrder(root *TreeNode) [][]int {
   result := make([][]int, 0)
   if root == nil {
      return result
   }
   stk := []*TreeNode{root}
   level := 1
   for len(stk) != 0 {
      length := len(stk)
      vals := make([]int, length)
      tmp := []*TreeNode{}
      for i := 0; i < length; i++ {
         if stk[i] == nil{
            continue
         }
         if level%2 != 0 {
            vals[i] = stk[i].Val
         } else {
            vals[length-1-i] = stk[i].Val
         }
         if stk[i].Left != nil {
            tmp = append(tmp, stk[i].Left)
         }
         if stk[i].Right != nil {
            tmp = append(tmp, stk[i].Right)
         }
      }
      stk = tmp
      result = append(result, vals)
      level += 1
   }
   return result
}
```
