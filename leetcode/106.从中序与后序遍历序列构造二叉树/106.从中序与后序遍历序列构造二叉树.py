from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder: List[int], in_start: int, in_end: int,
              postorder: List[int], post_start: int, post_end: int):
        if post_start > post_end:
            return None
        root_val = postorder[post_end]
        index = 0
        for i in range(in_start, in_end + 1):
            if inorder[i] == root_val:
                index = i
                break
        left_size = index - in_start
        root = TreeNode(val=root_val)
        root.left = self.build(inorder, in_start, index - 1, postorder, post_start, post_start + left_size - 1)
        root.right = self.build(inorder, index + 1, in_end, postorder, post_start + left_size, post_end - 1)
        return root
