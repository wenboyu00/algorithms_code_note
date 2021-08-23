# 题目
<p>给你一棵以 <code>root</code> 为根的 <strong>二叉树</strong> ，请你返回 <strong>任意</strong> 二叉搜索子树的最大键值和。</p>

<p>二叉搜索树的定义如下：</p>

<ul>
	<li>任意节点的左子树中的键值都 <strong>小于</strong> 此节点的键值。</li>
	<li>任意节点的右子树中的键值都 <strong>大于</strong> 此节点的键值。</li>
	<li>任意节点的左子树和右子树都是二叉搜索树。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/07/sample_1_1709.png" style="height: 250px; width: 320px;" /></p>

<pre>
<strong>输入：</strong>root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
<strong>输出：</strong>20
<strong>解释：</strong>键值为 3 的子树是和最大的二叉搜索树。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/07/sample_2_1709.png" style="height: 180px; width: 134px;" /></p>

<pre>
<strong>输入：</strong>root = [4,3,null,1,2]
<strong>输出：</strong>2
<strong>解释：</strong>键值为 2 的单节点子树是和最大的二叉搜索树。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [-4,-2,-5]
<strong>输出：</strong>0
<strong>解释：</strong>所有节点键值都为负数，和最大的二叉搜索树为空。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>root = [2,1,3]
<strong>输出：</strong>6
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>root = [5,4,8,3,null,6,3]
<strong>输出：</strong>7
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>每棵树有 <code>1</code> 到 <code>40000</code> 个节点。</li>
	<li>每个节点的键值在 <code>[-4 * 10^4 , 4 * 10^4]</code> 之间。</li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉搜索树</li><li>动态规划</li><li>二叉树</li></div></div>

# Python

```python
class Solution:
    def __init__(self):
        self.max_sum = 0

    def maxSumBST(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.max_sum

    def traverse(self, root: TreeNode):
        """
        返回一个4位数组 res
        res[0] 以 root 为根的二叉树是否是 BST，1 是 BST，0 不是 BST；
        res[1] 以 root 为根的二叉树所有节点中的最小值；
        res[2] 以 root 为根的二叉树所有节点中的最大值；
        res[3] 以 root 为根的二叉树所有节点值之和。
        """
        # base case
        # 任何一个单独节点就是BST,所以返回res[0] = 1
        if root is None:
            return [1, float('INF'), float('-INF'), 0]
        # 递归左右子树
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        # 后序遍历位置
        res = [0] * 4
        # 判断以root为根的二叉树是不是BST
        if left[0] == 1 and right[0] == 1 and left[2] < root.val < right[1]:
            # 以root为根的二叉树是BST
            res[0] = 1
            # 计算以root为根的BST最小值/最大值
            res[1] = min(left[1], root.val)
            res[2] = max(right[2], root.val)
            # 计算以root为根的这颗BST所有节点之和
            res[3] = left[3] + right[3] + root.val
            # 更新全局变量
            self.max_sum = max(self.max_sum, res[3])
        else:
            res[0] = 0
        return res
```

# Go

```go
func maxSumBST(root *TreeNode) int {
   maxSum := 0
   var traverse func(root *TreeNode) []int
   traverse = func(root *TreeNode) []int {
      /*
      res是4个值的数组
      res[0] 以root为根的二叉树是否为bst，1是，0否
      res[1] 以root为根的二叉树所有节点的最小值
      res[2] 以root为根的二叉树所有节点的最大值
      res[3] 以root为根的二叉树所有节点值之和
      */
      // base case
      if root == nil {
         return []int{1, math.MaxInt64, math.MinInt64, 0}
      }
      left := traverse(root.Left)
      right := traverse(root.Right)
      res := []int{0, 0, 0, 0}
      if left[0] == 1 && right[0] == 1 && left[2] < root.Val && right[1] > root.Val {
         res[0] = 1
         res[1] = min(left[1], root.Val)
         res[2] = max(right[2], root.Val)
         res[3] = left[3] + right[3] + root.Val
         maxSum = max(maxSum, res[3])
      } else
      {
         res[0] = 0
      }
      return res
   }
   traverse(root)
   return maxSum
}
```