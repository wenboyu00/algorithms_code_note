class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = 0

    def maxSumBST(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.max_sum

    def traverse(self, root: TreeNode):
        """
        返回一个4位数组 res
        res[0] 以 root 为根的二叉树是否是 BST，1 是 BST，0 不是 BST；
        res[1] 以 root 为根的二叉树所有节点中的最小值；
        res[2] 以 root 为根的二叉树所有节点中的最大值；
        res[3] 以 root 为根的二叉树所有节点值之和。
        """
        # base case
        # 任何一个单独节点就是BST,所以返回res[0] = 1
        if root is None:
            return [1, float('INF'), float('-INF'), 0]
        # 递归左右子树
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        # 后序遍历位置
        res = [0] * 4
        # 判断以root为根的二叉树是不是BST
        if left[0] == 1 and right[0] == 1 and left[2] < root.val < right[1]:
            # 以root为根的二叉树是BST
            res[0] = 1
            # 计算以root为根的BST最小值/最大值
            res[1] = min(left[1], root.val)
            res[2] = max(right[2], root.val)
            # 计算以root为根的这颗BST所有节点之和
            res[3] = left[3] + right[3] + root.val
            # 更新全局变量
            self.max_sum = max(self.max_sum, res[3])
        else:
            res[0] = 0
        return res

