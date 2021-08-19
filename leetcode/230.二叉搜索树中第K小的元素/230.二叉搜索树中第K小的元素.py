class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    根据BST的特性，左小右大，子树依然，使用中序遍历找到第k个数
    """

    def __init__(self):
        self.res = 0
        # 排名
        self.rank = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if root is None:
            return root
        self.traverse(root, k)
        self.rank += 1
        if k == self.rank:
            self.res = root.val
        self.traverse(root, k)
