class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def convertBST(self, root: TreeNode) -> TreeNode:

        def convert(node: TreeNode):
            if node is None:
                return
            convert(node.right)
            self.count += node.val
            node.val = self.count
            convert(node.left)

        convert(root)
        return root

