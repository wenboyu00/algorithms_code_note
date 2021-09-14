class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        slow = fast = head
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        # 断开与后面重复元素的连接
        slow.next = None
        return head
