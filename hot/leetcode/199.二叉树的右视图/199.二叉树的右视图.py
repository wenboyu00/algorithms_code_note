from typing import List, Optional

from util.leetcode_type import TreeNode


class Solution:
    """
    递归顺序根右左，每层都是最先访问最右边的节点
    当前深度==len(self.ans)，说明当前层节点还没有出现在结果中，添加节点到结果中
    """

    def __init__(self):
        self.ans = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, depth):
        if not root:
            return root
        # 根右左递归
        if depth == len(self.ans):
            self.ans.append(root.val)

        depth += 1
        self.dfs(root.right, depth)
        self.dfs(root.left, depth)
