# 题目
<p>给定一棵树的前序遍历 <code>preorder</code> 与中序遍历  <code>inorder</code>。请构造二叉树并返回其根节点。</p>

<p> </p>

<p><strong>示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" />
<pre>
<strong>Input:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>Input:</strong> preorder = [-1], inorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p> </p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 <= preorder.length <= 3000</code></li>
	<li><code>inorder.length == preorder.length</code></li>
	<li><code>-3000 <= preorder[i], inorder[i] <= 3000</code></li>
	<li><code>preorder</code> 和 <code>inorder</code> 均无重复元素</li>
	<li><code>inorder</code> 均出现在 <code>preorder</code></li>
	<li><code>preorder</code> 保证为二叉树的前序遍历序列</li>
	<li><code>inorder</code> 保证为二叉树的中序遍历序列</li>
</ul>
<div><div>Related Topics</div><div><li>树</li><li>数组</li><li>哈希表</li><li>分治</li><li>二叉树</li></div></div>

# Python

```python
class Solution:
    """
    画 前序和中序 图，确定索引位置关系，递归构建
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 通过前序和中序规律来递归构造二叉树
        return self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(preorder) - 1)

    def build(self, preorder: List[int], pre_start: int, pre_end: int,
              inorder: List[int], in_start: int, in_end: int):
        # start=end是结束
        if pre_start > pre_end:
            return None
        # 前序[0]是根节点
        root_val = preorder[pre_start]
        index = 0
        # 通过根值，找到中序根的位置，分割数组
        for i in range(in_start, in_end + 1):
            if inorder[i] == root_val:
                index = i
                break
        # 中序是 左根右，在数组中 根的左边是左子树，根的index-中序的开始 就是左子树长度
        left_size = index - in_start
        root = TreeNode(root_val, None, None)
        # 构造左子树
        # - 前序，根左右，左子树起始：根节点+1；左子树终点：左子树起点+左子树长度
        # - 中序，左根右，左子树起始：原起始值，左子树终点：根节点-1
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, index - 1)
        # 构造右子树
        # - 前序，右子树起始：左子树起始+左子树+1(跳过左子树终点）， 终点：原终止点
        # - 中序，右子树起始：根节点+1（跳过根节点），终点：原终止点
        root.right = self.build(preorder, pre_start + left_size + 1, pre_end,
                                inorder, index + 1, in_end)

        return root
```

# Go

```go
func buildTree(preorder []int, inorder []int) *TreeNode {
   return build(preorder, 0, len(preorder)-1,
      inorder, 0, len(inorder)-1)
}

func build(preorder []int, preStart int, preEnd int,
   inorder []int, inStart int, inEnd int) *TreeNode {
   if preStart > preEnd {
      return nil
   }
   rootVal := preorder[preStart]
   index := 0
   for i := inStart; i <= inEnd; i++ {
      if inorder[i] == rootVal {
         index = i
         break
      }
   }
   leftSize := index - inStart
   root := &TreeNode{Val: rootVal}
   root.Left = build(preorder, preStart+1, preStart+leftSize, inorder, inStart, index-1)
   root.Right = build(preorder, preStart+leftSize+1, preEnd, inorder, index+1, inEnd)
   return root
}
```