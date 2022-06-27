class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""
题目要求深拷贝
深拷贝 = 新建节点，关系一致
难点：新建时保持原有的节点关系
解决方法：哈希法，原节点映射拷贝节点 [原节点]  = [拷贝节点]
流程：
1. 拷贝节点，并建立原节点和拷贝节点关系
2. 根据原节点的关系，赋值拷贝节点的关系（next和random)
    a. 拷贝节点.next参考原节点.next指向的节点
    b. map.get(cur).next  是拷贝节点.next
    c. cur.next 是原节点.next指向的节点
    d. map.get(cur.next) 原节点.next节点映射的拷贝节点
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 原节点和拷贝节点映射表  [原节点] = 拷贝节点
        ori_copy_map = dict()
        cur = head
        # 拷贝节点值，并增加对应关系
        while cur:
            ori_copy_map[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        # 根据原节点的关系，赋值拷贝节点的关系
        while cur:
            # 拷贝节点的next = 原节点next 映射的拷贝节点
            ori_copy_map.get(cur).next = ori_copy_map.get(cur.next)
            # 拷贝节点的random = 原节点random 映射的拷贝节点
            ori_copy_map.get(cur).random = ori_copy_map.get(cur.random)
            cur = cur.next
        return ori_copy_map.get(head)
