from typing import Optional

from util.leetcode_type import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        self.max_path(root)
        return self.ans

    def max_path(self, root):
        """
        1. 把当前节点和左右节点中最大的作为路径的一部分，作为路径和返回
        - 从左右节点中选择路径和最大的+ 当前节点 = 新的节点和返回
        2. 更新最大路径和答案
        比较答案和当前的路径和 = 左右子数路径和+当前路径val
        """
        # base case 为空是值为0
        if root is None:
            return 0
        # 获取左右子树最大路径和
        left = max(0, self.max_path(root.left))
        right = max(0, self.max_path(root.right))
        # 更新答案
        self.ans = max(self.ans, left + root.val + right)
        # 返回当前路径和
        return root.val + max(left, right)
