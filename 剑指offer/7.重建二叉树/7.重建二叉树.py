from typing import List

from util.leetcode_type import TreeNode

"""
前序:根左右，中序:左右根。

递归结束条件：
因为前序列表查询，如果start=end说明已经完成。所以，start>end

递归过程:
找到前序根，再找中序根位置
中序根位置 - 中序开始位置就是左子树的长度
分割前序左子树和中序左子树
    - 前序：start= start+1，end = start+left_size
    - 中序: start = start, end = index-1
分割前序右子树和中序右子树
    分割前序左子树和中序左子树
    - 前序：start= start+left_size+1，end = end
    - 中序: start = index+1, end = end
生成节点并给左右子树赋值
最后返回节点
    

"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self._build_tree(preorder=preorder, pre_start=0, pre_end=len(preorder) - 1,
                                inorder=inorder, in_start=0, in_end=len(inorder) - 1,
                                )

    def _build_tree(self, preorder: List[int], pre_start: int, pre_end: int,
                    inorder: List[int], in_start: int, in_end: int) -> TreeNode:
        if pre_start > pre_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        index = 0
        # 找到中根的位置
        for i in range(in_start, in_end + 1):
            if inorder[i] == root_val:
                index = i
        left_size = index - in_start
        root.left = self._build_tree(preorder, pre_start + 1, pre_start + left_size,
                                     inorder, in_start, index - 1)
        root.right = self._build_tree(preorder, pre_start + left_size + 1, pre_end,
                                      inorder, index + 1, in_end)
        return root
