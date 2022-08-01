class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        # dummy节点用来辅助删除头节点，slow=dummy 同理
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy.next
        # fast前进n步
        for i in range(n):
            fast = fast.next
        # fast到达尾部时，slow刚好是 n-1位置
        while fast:
            fast = fast.next
            slow = slow.next
        # slow.nex是n位置的节点，删除
        slow.next = slow.next.next

        return dummy.next
