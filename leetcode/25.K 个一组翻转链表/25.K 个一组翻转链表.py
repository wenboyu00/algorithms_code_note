# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head


    def reverseAB(self, a: ListNode, b: ListNode):
        pre, cur = None, a
        while a != b:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp
        return pre

