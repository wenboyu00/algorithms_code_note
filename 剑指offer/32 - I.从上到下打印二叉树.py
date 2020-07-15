# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
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
#  返回：
#
#  [3,9,20,15,7]
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result, current = [], [root]
        while current:
            next_level = []
            for node in current:
                result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current = next_level
        return result
# leetcode submit region end(Prohibit modification and deletion)
