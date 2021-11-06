from util.leetcode_type import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        前缀和，回溯算法
        两个节点之差等于 targetSum 即可
        """
        # 记录路径中前缀和出现次数
        # base case 开始是0出现1
        mapping = {0: 1}

        def dfs(root, cur):
            # 结束条件
            if not root:
                return
            # 前缀和+当前节点值
            cur += root.val
            # 判断是否存在符合条件的前缀和
            pre = cur - targetSum
            self.res += mapping.get(pre, 0)
            # 记录当前前缀和
            mapping[cur] = mapping.get(cur, 0) + 1
            dfs(root.left, cur)
            dfs(root.right, cur)
            # 回溯，恢复状态
            mapping[cur] -= 1

        dfs(root, 0)
        return self.res
