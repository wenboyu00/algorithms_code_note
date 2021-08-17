class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.successor = None

    # 反转以head为开始第left到right个节点，并返回头节点
    # 把反转一部分，分解为：前进到反转起点+反转起点后n个节点
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # base case
        if left == 1:
            # 反转起点后n个节点
            return self.reverseN(head, right)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    # 反转以 head 为起点的 n 个节点，返回新的头结点
    def reverseN(self, head: ListNode, n: int):
        # 记录第n + 1个节点，反转之后将head.next = successor
        if n == 1:
            self.successor = head.next
            return head
        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.successor
        return last
