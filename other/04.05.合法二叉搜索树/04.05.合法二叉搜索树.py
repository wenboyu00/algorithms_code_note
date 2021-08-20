class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #  限定以 root 为根的子树节点必须满足 min.val < root.val < max.val
        def is_valid_bst(root: TreeNode, min_val: int, max_val: int) -> bool:
            # base case 用于结束递归，root不存在也就是合法
            if root is None:
                return True
            # 合法时进行递归，不合法返回False
            if min_val < root.val < max_val:
                # 限定左子树最大值是root.val
                # 限定右子树最小值是root.val，符合BST规则
                return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)
            else:
                return False

        return is_valid_bst(root, float('-INF'), float('INF'))
