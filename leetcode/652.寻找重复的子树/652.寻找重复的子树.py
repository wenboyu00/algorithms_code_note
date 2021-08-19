from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        # 存储子树描述字符串，用数量去重，每个子树只有1个
        self.momo = {}
        # 储存结果
        self.res = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.travers(root)
        return self.res

    def travers(self, root: TreeNode) -> str:
        # base case
        if root is None:
            return "#"
        # 用后序递归遍历，来描述子树
        left = self.travers(root.left)
        right = self.travers(root.right)
        sub_tree = f'{left},{right},{root.val}'
        # 获得子树字符串在出现次数
        freq = self.momo.get(sub_tree, 0)
        # 为1时，找到相同的树，结果+1，出现次数+1
        if freq == 1:
            self.res.append(root)
        self.momo[sub_tree] = freq + 1

        return sub_tree
