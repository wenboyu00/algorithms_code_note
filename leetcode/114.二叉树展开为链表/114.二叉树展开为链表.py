class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return None
        # 后序遍历
        self.flatten(root.left)
        self.flatten(root.right)
        # 1.左右子树拉平成一条链表
        left = root.left
        right = root.right
        # 2.将左子树移到右子树上
        root.left = None
        root.right = left
        # 3.将原root右子树接到当前右子树（原左子树）末端
        #  - 找到现右子树最后一个节点，把原右子树街上
        p = root
        while p.right is not None:
            p = p.right
        p.right = right
