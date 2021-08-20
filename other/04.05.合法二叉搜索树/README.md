# 题目
<p>实现一个函数，检查一棵二叉树是否为二叉搜索树。</p><strong>示例 1:</strong><pre><strong>输入:</strong><br>    2<br>   / &#92<br>  1   3<br><strong>输出:</strong> true<br></pre><strong>示例 2:</strong><pre><strong>输入:</strong><br>    5<br>   / &#92<br>  1   4<br>     / &#92<br>    3   6<br><strong>输出:</strong> false<br><strong>解释:</strong> 输入为: [5,1,4,null,null,3,6]。<br>     根节点的值为 5 ，但是其右子节点值为 4 。</pre><div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉搜索树</li><li>二叉树</li></div></div>



# Python

```python
def isValidBST(self, root: TreeNode) -> bool:
    #  限定以 root 为根的子树节点必须满足 min.val < root.val < max.val
    def is_valid_bst(root: TreeNode, min_val: int, max_val: int) -> bool:
        # base case 用于结束递归，root不存在也就是合法
        if root is None:
            return True
        # 合法时进行递归，不合法返回False
        if min_val < root.val < max_val:
            # 限定左子树最大值是root.val
            # 限定右子树最小值是root.val，符合BST规则
            return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)
        else:
            return False

    return is_valid_bst(root, float('-INF'), float('INF'))
```

# Go

```go
func isValidBST(root *TreeNode) bool {

   var isValid func(root *TreeNode, min int, max int) bool
   isValid = func(root *TreeNode, min int, max int) bool {
      if root == nil {
         return true
      }
      if min < root.Val && root.Val < max {
         // 左子树最大值：root.val；右子树最小值:root.val
         return isValid(root.Left, min, root.Val) && isValid(root.Right, root.Val, max)
      } else {
         return false
      }

   }
   return isValid(root, math.MinInt64, math.MaxInt64)
}
```