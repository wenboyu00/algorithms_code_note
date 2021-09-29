from util.leetcode_type import TreeNode


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        cur = TreeNode(root1.val + root2.val)
        cur.left = self.mergeTrees(root1.left, root2.left)
        cur.right = self.mergeTrees(root1.right, root2.right)
        return cur
