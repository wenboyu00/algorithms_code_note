from util.leetcode_type import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # fast 节点先前进 k
        # slow, fast同步前进，fast到队尾时 slow就是第k个节点
        fast, slow = head, head
        for i in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
