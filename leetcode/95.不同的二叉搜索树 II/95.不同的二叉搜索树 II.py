from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.generate(1, n)

    def generate(self, low, high) -> List[TreeNode]:
        res = []
        if low > high:
            res.append(None)
            return res
        for i in range(low, high + 1):
            # 递归构造左右子树
            left = self.generate(low, i - 1)
            right = self.generate(i + 1, high)
            # 给root节点穷举所有左右子树
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
