class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # base case
        if root is None:
            return root
        if root.val == key:
            # 如果不存在左节点，返回右节点
            # 如果不存在右节点，返回左节点
            # 两个不存在也是返回的None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 处理 左右子树都存在，查找右子树最小并对值进行替换
            min_node = self.findMin(root.right)
            root.val = min_node.val
            # 删除替换的最小节点
            root.right = self.deleteNode(root.right, min_node.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
