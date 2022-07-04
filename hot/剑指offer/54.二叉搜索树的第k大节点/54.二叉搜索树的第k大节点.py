from util.leetcode_type import TreeNode

"""
bst,前序是从小到大，后序是从大到小，给后续遍历节点计数，count==k时，则为k大的数
"""


class Solution:
    def __init__(self):
        self.count = 0
        self.result = -1

    def kthLargest(self, root: TreeNode, k: int) -> int:

        self.traverse(root, k)
        return self.result

    def traverse(self, root, k):
        if root is None:
            return root
        self.traverse(root.right, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
        self.traverse(root.left, k)
