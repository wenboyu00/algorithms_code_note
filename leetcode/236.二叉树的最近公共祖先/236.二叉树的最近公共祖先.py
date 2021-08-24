class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
1.此函数是干什么的？
    输入 root , p , q, 返回一个节点
    情况1，如果p和q都是以root为根的树中，返回root
    情况2，如果p和q都不在root为根的树中，返回None
    情况3，如果p或者q 在以root为根的书中，返回存在节点  
    情况2和情况3合并返回：
        - 如果left is None  返回right 反之依然；
        - 保证能返回在以root为根的树中节点和都不存在的情况了
2.函数的参数是干什么的？
函数遍历是root，主要用于"状态转移"为root.left和root.right
p和q 是固定值
3.递归得到结果该干什么？
递归调用后，做什么”选择“
base case
    - root 为None，返回None
    - root == p或者q，返回root
        - 如果 p 或 q 等于root，说明此节点存在root为根的树中，root就是最近的公共祖先
4.遍历顺序？
因为需要左右子树来确定根的状态，所以使用后序遍历
后序遍历是从下到上遍历
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 后续遍历
        # base case
        # 节点为空返回空
        # 如果 p 或 q 等于root，说明此节点存在root为根的树中，root就是最近的公共祖先
        if root is None:
            return root
        if root == q or root == p:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 情况1，p和q都是以root为根的树中，left和right一定分别是p和q
        if left and right:
            return root
        # 情况2和3，p和q都不是，或者其中一个是并返回
        # left不是，返回right，right不是返回left，如果两个都不是，那么返回后也是None
        if left is None:
            return right
        if right is None:
            return left
