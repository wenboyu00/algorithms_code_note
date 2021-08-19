# 题目
<p>根据一棵树的中序遍历与后序遍历构造二叉树。</p>

<p><strong>注意:</strong><br>
你可以假设树中没有重复的元素。</p>

<p>例如，给出</p>

<pre>中序遍历 inorder =&nbsp;[9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]</pre>

<p>返回如下的二叉树：</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>
<div><div>Related Topics</div><div><li>树</li><li>数组</li><li>哈希表</li><li>分治</li><li>二叉树</li></div></div>

# Python

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder: List[int], in_start: int, in_end: int,
              postorder: List[int], post_start: int, post_end: int):
        if post_start > post_end:
            return None
        root_val = postorder[post_end]
        index = 0
        for i in range(in_start, in_end + 1):
            if inorder[i] == root_val:
                index = i
                break
        left_size = index - in_start
        root = TreeNode(val=root_val)
        root.left = self.build(inorder, in_start, index - 1, postorder, post_start, post_start + left_size - 1)
        root.right = self.build(inorder, index + 1, in_end, postorder, post_start + left_size, post_end - 1)
        return root
```

# Go

```go
func buildTree(inorder []int, postorder []int) *TreeNode {
   return build(inorder, 0, len(inorder)-1,
      postorder, 0, len(postorder)-1)
}
func build(inorder []int, inStart int, inEnd int,
   postorder []int, postStart int, postEnd int) *TreeNode {
   if postStart > postEnd {
      return nil
   }
   // 后序[-1]是根节点
   rootVal := postorder[postEnd]
   index := 0
   for i := inStart; i <= inEnd; i++ {
      if inorder[i] == rootVal {
         index = i
         break
      }
   }
   leftSize := index - inStart
   root := &TreeNode{Val: rootVal}
   // 构造左子树
   // - 中序，左右根，左子树起始：原起始值，右子树终点：根节点-1（跳过根节点）
   // - 后序，根左右，左子树起始：原起始值；左子树终点：左子树起点+左子树长度-1（跳过右子树起点）
   root.Left = build(inorder, inStart, index-1, postorder, postStart, postStart+leftSize-1)
   // 构造右子树
   // - 中序，右子树起始：根节点+1（跳过根节点）；右子树终点：原终点
   // - 后序，右子树起始：左子树起点+左子树长度；右子树终点：根节点-1（跳过根节点）
   root.Right = build(inorder, index+1, inEnd, postorder, postStart+leftSize, postEnd-1)

   return root
}
```