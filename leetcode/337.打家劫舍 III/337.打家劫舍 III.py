# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
