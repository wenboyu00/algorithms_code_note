class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
二叉搜索树，中序遍历 从小到大
双向链表：在构建相邻节点的引用关系时，设前驱节点 pre 和当前节点 cur ，不仅应构建 pre.right = cur ，也应构建 cur.left = pre
循环链表：头结点head和尾节点tail，应构建 head.left = tail 和 tail.right = head 
    - 在没有前驱节点时 当前节点就是头结点
    - 结尾时，pre就是尾节点
"""


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def build(cur):
            if not cur:
                return cur
            # 二叉搜索树，中序遍历
            build(cur.left)
            # 建立双向链表
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            # 没有前驱节点时，当前节点就是头节点
            else:
                self.head = cur
            # 递归时，当前节点为前驱节点
            self.pre = cur
            build(cur.right)

        if not root:
            return root
        build(root)
        # 构建循环链表头尾节点引用关系
        self.pre.right = self.head
        self.head.left = self.pre
        return self.head
