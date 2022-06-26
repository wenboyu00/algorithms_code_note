from util.leetcode_type import ListNode

"""
dummy作为head前节点 方便返回内容
pre作为cur的前节点，方便删除cur的内容
"""

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            cur = cur.next
            pre = pre.next
        return dummy.next
