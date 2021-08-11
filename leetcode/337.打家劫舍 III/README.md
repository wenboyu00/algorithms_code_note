# 题目
<p>在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为&ldquo;根&rdquo;。 除了&ldquo;根&rdquo;之外，每栋房子有且只有一个&ldquo;父&ldquo;房子与之相连。一番侦察之后，聪明的小偷意识到&ldquo;这个地方的所有房屋的排列类似于一棵二叉树&rdquo;。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。</p>

<p>计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[3,2,3,null,3,null,1]

     <strong>3</strong>
    / \
   2   3
    \   \ 
     <strong>3</strong>   <strong>1</strong>

<strong>输出:</strong> 7 
<strong>解释:</strong>&nbsp;小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = <strong>7</strong>.</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[3,4,5,1,3,null,1]

&nbsp;    3
    / \
   <strong>4</strong>   <strong>5</strong>
  / \   \ 
 1   3   1

<strong>输出:</strong> 9
<strong>解释:</strong>&nbsp;小偷一晚能够盗取的最高金额&nbsp;= <strong>4</strong> + <strong>5</strong> = <strong>9</strong>.
</pre>

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>动态规划</li><li>二叉树</li></div></div>

# Python

```python
def rob(self, root: TreeNode) -> int:
    memo = {}

    def do_rob(root: TreeNode) -> int:
        if root is None:
            return 0
        if root in memo:
            return memo[root]

        rob_val_l, rob_val_r = 0, 0
        if root.left is not None:
            # 因为是二叉树，下下个节点 分别为 根左左，根左右
            rob_val_l = do_rob(root.left.left) + do_rob(root.left.right)
        if root.right is not None:
            # 因为是二叉树，下下个节点 分别为 根右左，根右右
            rob_val_r = do_rob(root.right.left) + do_rob(root.right.right)
        # 打劫此节点 + 下下个节点
        do_it = root.val + rob_val_l + rob_val_r
        # 不打劫此节点+ 打劫下个节点
        not_do_it = do_rob(root.left) + do_rob(root.right)
        # 取出最有价值的路线
        res = max(do_it, not_do_it)
        # 存入dp数组
        memo[root] = res
        return res

    return do_rob(root)
```

# Go

```go
func rob(root *TreeNode) int {
   memo := make(map[*TreeNode]int)
   return doRob(root, memo)
}

func doRob(root *TreeNode, memo map[*TreeNode]int) int {
   if root == nil {
      return 0
   }
   if val, ok := memo[root]; ok {
      return val
   }
   doItL := 0
   doItR := 0
   if root.Left != nil{
      doItL = doRob(root.Left.Left, memo) + doRob(root.Left.Right, memo)
   }
   if root.Right != nil{
      doItR = doRob(root.Right.Left, memo) + doRob(root.Right.Right, memo)
   }
   doIt := root.Val + doItL + doItR
   notDoIt := doRob(root.Left, memo) + doRob(root.Right, memo)
   res := max(doIt, notDoIt)
   memo[root] = res
   return res
}
```