# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
#
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#  1
#  / \
#  2 2
#  / \ / \
# 3 4 4 3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#  1
#  / \
#  2 2
#  \ \
#  3 3
#
#
#
#  示例 1：
#
#  输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
#  示例 2：
#
#  输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 1000
#
#  注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        return self._is_mirror(root, root)

    def _is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        return self._is_mirror(left.left, right.right) and \
               self._is_mirror(left.right, right.left)
# leetcode submit region end(Prohibit modification and deletion)
