from util.leetcode_type import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 穿针引线，初始化链表头和尾
        # 用尾节点去链接新的节点，谁小就链接上，同时新链表和对应链表进一步
        # 最后还有值的链表全部接到新链表后面
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l2:
            tail.next = l2
        if l1:
            tail.next = l1
        return dummy.next
