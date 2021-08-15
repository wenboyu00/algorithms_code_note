# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        self.connect_two_node(root.left, root.right)
        return root

    def connect_two_node(self, node1: 'Node', node2: 'Node'):
        if node1 is None or node2 is None:
            return None
        # 前序遍历
        # 将传入的两个节点相连
        node1.next = node2
        # 连接相同父节点的两个子节点
        self.connect_two_node(node1.left, node1.right)
        self.connect_two_node(node2.left, node2.right)
        # 连接跨父节点的两个子节点
        self.connect_two_node(node1.right, node2.left)
