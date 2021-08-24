import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # 求左右子树高度
        left = right = root
        left_high = right_high = 0
        while left:
            left = left.left
            left_high += 1
        while right:
            right = right.right
            right_high += 1
        # 如果左右子树相同是满二叉树
        # 满二叉树节点总数 = 2^high -1
        if left_high == right_high:
            return int(math.pow(2, left_high)) - 1
        # 普通二叉树进入递归相加，1是为当前节点
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
