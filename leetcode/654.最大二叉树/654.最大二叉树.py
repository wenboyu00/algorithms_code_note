from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 找到对应nums最大值和对应索引
        # 然后递归调用左右数组来构建左右子树即可
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], low: int, high: int):
        # 在数组中范围内，找到最大值作为根节点，并构建左右子树
        if low > high:
            return None
        max_val = float('-INF')
        index = 0
        # 在low,high范围内[low,high]，找到最大值max_val和索引index
        for i in range(low, high + 1):
            if nums[i] > max_val:
                max_val = nums[i]
                index = i
        # 初始化根
        root = TreeNode(max_val, None, None)
        # 调用左右数组来构建左右字数，
        root.left = self.build(nums, low, index - 1)
        root.right = self.build(nums, index + 1, high)
        return root


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    result = Solution().constructMaximumBinaryTree(nums)
    print(result)
