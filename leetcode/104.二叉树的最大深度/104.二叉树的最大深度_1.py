from util.leetcode_type import TreeNode


# 广度优先，迭代方式
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stk = []
        depth = 0
        if root:
            stk.append((1, root))
        while stk:
            cur_depth, node = stk.pop()
            if node:
                stk.append((cur_depth + 1, node.left))
                stk.append((cur_depth + 1, node.right))
                depth = max(cur_depth, depth)
        return depth
