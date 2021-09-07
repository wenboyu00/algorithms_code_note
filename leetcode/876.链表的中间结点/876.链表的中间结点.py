class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
