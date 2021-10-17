from util.leetcode_type import ListNode


class Solution:
    """
    时间复杂度要求：nlogn 考虑二分法-归并排序
        归并排序分为：
        递归方式：
        先分割，然后归并时排序
            - 归并-leetcode.21题-合并两个有序链表
                - 遍历两个链表节点，比较值大小，小的加入链表，交替进行
            - 分割-leetcode.876题-找到链表中点
                - 找到中点进行拆分
                - 使用快慢指针，要找到第一个中值，指针初始不一致
    """

    def sortList(self, head: ListNode) -> ListNode:
        # 先分割
        # base case，head和head.next 存在才排序的必要
        if not head or not head.next:
            return head
        # 快慢指针
        # 初始化不一致，slow在偶数时找到第一个中值
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 从中间分割成2个链表
        mid = slow.next
        slow.next = None
        # 对链表进行排序
        return self.megre(self.sortList(head), self.sortList(mid))

    def megre(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            # 把l1交换成小值节点
            if l1.val > l2.val:
                l1, l2 = l2, l1
            # tail.next指向小值节点
            tail.next = l1
            # 前进一步
            l1 = l1.next
            tail = tail.next
        # tail接上剩下的节点
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
