# 题目
<p>给定一个二叉树的根节点 <code>root</code> ，和一个整数 <code>targetSum</code> ，求该二叉树里节点值之和等于 <code>targetSum</code> 的 <strong>路径</strong> 的数目。</p>

<p><strong>路径</strong> 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg" style="width: 452px; " /></p>

<pre>
<strong>输入：</strong>root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
<strong>输出：</strong>3
<strong>解释：</strong>和等于 8 的路径有 3 条，如图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示:</strong></p>

<ul>
	<li>二叉树的节点个数的范围是 <code>[0,1000]</code></li>
	<li><meta charset="UTF-8" /><code>-10<sup>9</sup> <= Node.val <= 10<sup>9</sup></code> </li>
	<li><code>-1000 <= targetSum <= 1000</code> </li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉树</li></div></div><br><div>

# Python

```python
def __init__(self):
    self.res = 0

def pathSum(self, root: TreeNode, targetSum: int) -> int:
    """
    前缀和，回溯算法
    两个节点之差等于 targetSum 即可
    """
    # 记录路径中前缀和出现次数
    # base case 开始是0出现1
    mapping = {0: 1}

    def dfs(root, cur):
        # 结束条件
        if not root:
            return
        # 前缀和+当前节点值
        cur += root.val
        # 判断是否存在符合条件的前缀和
        pre = cur - targetSum
        self.res += mapping.get(pre, 0)
        # 记录当前前缀和
        mapping[cur] = mapping.get(cur, 0) + 1
        dfs(root.left, cur)
        dfs(root.right, cur)
        # 回溯，恢复状态
        mapping[cur] -= 1

    dfs(root, 0)
    return self.res
```

# Go

```go
func pathSum(root *TreeNode, targetSum int) int {
   /*
   前缀和+dfs回溯
   计算路径上的前缀和，如果有路径和 - 目标值的差值 已经存在，说明有路径和，结果值加上差值的次数
   */
   // 存储路径和次数， base case：0出现1次
   mapping := map[int]int{0:1}
   res := 0
   var dfs func(root *TreeNode, cur int)
   dfs = func(root *TreeNode, cur int) {
      if root == nil {
         return
      }
      // 路径和，并记录到哈希表
      cur += root.Val
      mapping[cur] =+ 1
      // 计算路径和差值，并添加差值出现次数到结果中
      need := cur - targetSum
      res += mapping[need]
      // 递归左右子树
      dfs(root.Left, cur)
      dfs(root.Right, cur)
      // 删除当前路径出现次数
      mapping[cur] -= 1
   }
   dfs(root,0)
   return res
}
```