from util.leetcode_type import TreeNode


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        二叉树的直径：从一个节点到另一个节点最长的路径
        题目求：任意节点，所以要每次递归是都判断当前的路径是否是最大
        """

        def deep(root):
            if root is None:
                return 0
            left = deep(root.left)
            right = deep(root.right)
            # 判断此节点路径是否是最长
            self.ans = max(self.ans, left + right + 1)
            # 返回左右路径中最长+1
            return max(left, right)

        deep(root)
        return self.ans
