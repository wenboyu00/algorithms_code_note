class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
递归算法
base case:
    if head is None or head.next is None:
            return head
reverseList：会返回反转之后的头节点

head.next.next = head
    头节点下一个节点，指向头节点
head.next = None
    头节点指向None，完成反转
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 输入一个节点head，讲 “以head为起点”的链表反转，并返回反转之后的头节点
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return last
