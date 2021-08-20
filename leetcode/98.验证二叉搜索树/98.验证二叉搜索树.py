class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # bst 中序 从小到大，所有左子树小于根节点，所有右子树大于节点
    def isValidBST(self, root: TreeNode) -> bool:

        def is_valid_bst(root: TreeNode, min_val: int, max_val: int) -> bool:
            if root is None:
                return True
            if min_val < root.val < max_val:
                return is_valid_bst(root.left, min_val, root.val) and \
                       is_valid_bst(root.right, root.val, max_val)
            else:
                return False

        return is_valid_bst(root, float("-INF"), float("INF"))
