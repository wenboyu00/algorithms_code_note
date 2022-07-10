# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化头节点和尾节点
        dummy = tail = ListNode(0)
        # 两数相加累计值
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # s%10，取尾数
            tail.next = ListNode(s % 10)
            tail = tail.next
            # s//10，取位数之外的数，在这里是进位数
            s = s // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
