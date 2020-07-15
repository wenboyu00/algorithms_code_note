# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
#
#
#  例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层次遍历结果：
#
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
#
#
#
#  提示：
#
#
#  节点总数 <= 1000
#
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
            # 奇数时正序，偶数时倒序
            if level % 2:
                result.append(vals)
            else:
                result.append(vals[::-1])
            current = next_level
            level += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
