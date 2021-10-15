# 题目
<p>给你一个二叉树，请你返回其按 <strong>层序遍历</strong> 得到的节点值。 （即逐层地，从左到右访问所有节点）。</p>

<p> </p>

<p><strong>示例：</strong><br />
二叉树：<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回其层序遍历结果：</p>

<pre>
[
  [3],
  [9,20],
  [15,7]
]
</pre>
<div><div>Related Topics</div><div><li>树</li><li>广度优先搜索</li><li>二叉树</li></div></div>

# Python

```python
def levelOrder(self, root):
    """
    迭代遍历
    迭代时，通过数量来控制层数节点
    根据栈的情况迭代，
        - 每次循环通过取出节点总数把一层的节点遍历出来
        - 把节点的值添加到结果集中
        - 把节点子节点添加到栈中
    """
    if not root:
        return []
    res = []
    stk = [root]
    while stk:
        # 获取当前栈的长度，这个长度是这一层的节点数
        size = len(stk)
        nodes = []
        # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
        # 如果节点的左/右子树不为空，也放入队列中
        for i in range(size):
            node = stk.pop(0)
            nodes.append(node.val)
            # 添加子节点到栈中
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        # 将每层的节点值 添加到结果集中
        res.append(nodes)
    return res
```



# Go

```go
func levelOrder(root *TreeNode) [][]int {
   res := [][]int{}
   if root == nil {
      return res
   }
   stk := []*TreeNode{root}
   for len(stk) != 0 {
      vals := make([]int, 0, len(stk))
      nodes := append([]*TreeNode{}, stk...)
      stk = []*TreeNode{}
      for _, node := range nodes {
         vals = append(vals, node.Val)
         if node.Left != nil {
            stk = append(stk, node.Left)
         }
         if node.Right != nil {
            stk = append(stk, node.Right)
         }
      }
      res = append(res, append([]int{}, vals...))
   }
   return res
}
```