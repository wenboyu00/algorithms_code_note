class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    """
    画 前序和中序 图，确定索引位置关系，递归构建
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 通过前序和中序规律来递归构造二叉树
        return self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(preorder) - 1)

    def build(self, preorder: List[int], pre_start: int, pre_end: int,
              inorder: List[int], in_start: int, in_end: int):
        # start=end是结束
        if pre_start > pre_end:
            return None
        # 前序[0]是根节点
        root_val = preorder[pre_start]
        index = 0
        # 通过根值，找到中序根的位置，分割数组
        for i in range(in_start, in_end + 1):
            if inorder[i] == root_val:
                index = i
                break
        # 中序是 左根右，在数组中 根的左边是左子树，根的index-中序的开始 就是左子树长度
        left_size = index - in_start
        root = TreeNode(root_val, None, None)
        # 构造左子树
        # - 前序，根左右，左子树起始：根节点+1；左子树终点：左子树起点+左子树长度
        # - 中序，左根右，左子树起始：原起始值，左子树终点：根节点-1
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, index - 1)
        # 构造右子树
        # - 前序，右子树起始：左子树起始+左子树+1(跳过左子树终点）， 终点：原终止点
        # - 中序，右子树起始：根节点+1（跳过根节点），终点：原终止点
        root.right = self.build(preorder, pre_start + left_size + 1, pre_end,
                                inorder, index + 1, in_end)

        return root
