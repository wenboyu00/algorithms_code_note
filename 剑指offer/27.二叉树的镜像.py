# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#
#  例如输入：
#
#  4
#  / \
#  2 7
#  / \ / \
# 1 3 6 9
# 镜像输出：
#
#  4
#  / \
#  7 2
#  / \ / \
# 9 6 3 1
#
#
#
#  示例 1：
#
#  输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 1000
#
#  注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
1.先根遍历，遍历时对子节点交换
2.对已交换的节点进行递归调用
3.递归终止条件：当左右节点都不存在的时候，返回节点
"""
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.mirrorTree(root.left)
        if root.right:
            self.mirrorTree(root.right)
        return root
# leetcode submit region end(Prohibit modification and deletion)
