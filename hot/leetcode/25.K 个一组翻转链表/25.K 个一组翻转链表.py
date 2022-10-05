# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        k为一组反转链表
        递归反转k个节点
        1.定义a，b并赋值为head，b前进k个节点。反转a~b之间节点
        2.递归后续链表并连接起来
        """
        if head is None:
            return head
        # 区间[a,b)包含k个待反转
        a = b = head
        # b前进k个达到反转结束位置
        for i in range(k):
            # 不足k个，不需要反转 base case
            if b is None:
                return head
            b = b.next
        # 反转前k个元素
        new_head = self.reverseAB(a, b)
        # 递归反转后续链表并链接起来
        a.next = self.reverseKGroup(b, k)
        return new_head

    def reverseAB(self, a: ListNode, b: ListNode):
        # 反转区间[a,b)的元素，左闭右开
        pre, cur = None, a
        # cur = b 时终止，即a~(b-1)
        while cur != b:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp
        # 返回反转后头节点
        return pre
