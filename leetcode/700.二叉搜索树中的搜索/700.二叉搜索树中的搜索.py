class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 根据BST特性，左小右大，完成二分查找
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return root
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
