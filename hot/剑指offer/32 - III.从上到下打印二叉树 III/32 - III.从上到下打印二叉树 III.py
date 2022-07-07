from typing import List

from util.leetcode_type import TreeNode

"""
奇数正序，偶数倒序
每次外层循环，设置临时数组存放，在循环结束是判断层级奇偶来决定临时数组的结果倒序还是正序
"""


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result, current, level = [], [root], 1
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level % 2:
                result.append(vals)
            else:
                result.append(vals[::-1])
            current = next_level
            level += 1
        return result
