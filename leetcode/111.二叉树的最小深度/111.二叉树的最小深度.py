# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = list()
        q.append(root)
        depth = 1
        while len(q) != 0:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            depth += 1
