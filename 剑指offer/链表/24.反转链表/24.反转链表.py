from util.leetcode_type import ListNode

"""
递归
不进入递归中，只思考每次中的效果
递归结束条件：not cur and not cur.next
递归过程：
- 进入递归，把最后一个节点（当前的队尾，结果的队首）传递出去 last = self.reverse(cur.next)
- 当前节点下个的指向当前节点 cur.next.next = cur
- 取消之前指向 cur.next = None
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        return self.reverse(head)

    def reverse(self, cur):
        if not cur or not cur.next:
            return cur
        last = self.reverse(cur.next)
        cur.next.next = cur
        cur.next = None
        return last
