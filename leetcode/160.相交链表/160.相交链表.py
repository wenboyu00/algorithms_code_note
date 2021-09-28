from util.leetcode_type import ListNode


class Solution:
    """
    双指针解法，ab分别指向两个链表头部
    headA链表节点数为a，headB节点数为b
    两链表公共节点数为c
    a到c的距离为a-c, b到c的距离为b-c
    双指针如何同时到达c点？
    一样的距离，一样的速度
    所以：
        先走a再走b 距离为 a+(b-c)
        先走b再走c 距离为 b+(a-c)
    走的过距离相等，节点相等时，就是相交点
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != b:
            # 如果a没有了，就走b
            if a:
                a = a.next
            else:
                a = headB
            # 如果b没有了，就走a
            if b:
                b = b.next
            else:
                b = headA
        return a
