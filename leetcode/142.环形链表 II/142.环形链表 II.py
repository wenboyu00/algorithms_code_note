class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        meet_point = self.find_meet_point(head)
        if meet_point is None:
            return None

        fast = meet_point
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

    def find_meet_point(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow

        return None
