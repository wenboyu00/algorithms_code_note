# 题目


<p>给定一个二叉搜索树的根节点 <strong>root </strong>和一个值 <strong>key</strong>，删除二叉搜索树中的&nbsp;<strong>key&nbsp;</strong>对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。</p>

<p>一般来说，删除节点可分为两个步骤：</p>

<ol>
	<li>首先找到需要删除的节点；</li>
	<li>如果找到了，删除它。</li>
</ol>

<p><strong>说明：</strong> 要求算法时间复杂度为&nbsp;O(h)，h 为树的高度。</p>

<p><strong>示例:</strong></p>

<pre>
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7

<div><div>Related Topics</div><div><li>树</li><li>二叉搜索树</li><li>二叉树</li></div></div>

# Python

```python
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # base case
        if root is None:
            return root
        if root.val == key:
            # 如果不存在左节点，返回右节点
            # 如果不存在右节点，返回左节点
            # 两个不存在也是返回的None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 处理 左右子树都存在，查找右子树最小并对值进行替换
            min_node = self.findMin(root.right)
            root.val = min_node.val
            # 删除替换的最小节点
            root.right = self.deleteNode(root.right, min_node.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
```

# Go

```go
func deleteNode(root *TreeNode, key int) *TreeNode {
   if root == nil{
      return root
   }
   //找到值
   if root.Val == key{
      // 处理有一个子树，或者无子树时情况
      if root.Left == nil{
         return root.Right
      }
      if root.Right == nil{
         return root.Left
      }
      // 有双节点时，找到右子树最小的值，替换值，删除最小值的节点
      minNode := findMin(root.Right)
      root.Val = minNode.Val
      root.Right = deleteNode(root.Right, minNode.Val)
   }else if root.Val > key {
      root.Left = deleteNode(root.Left, key)
   }else if root.Val < key{
      root.Right = deleteNode(root.Right, key)
   }
   return root
}
func findMin(node *TreeNode) *TreeNode{
   for node.Left != nil{
      node = node.Left
   }
   return node
}
```