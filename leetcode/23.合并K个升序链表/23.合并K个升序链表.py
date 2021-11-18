from typing import List

from util.leetcode_type import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        在leetcode.21 合并两个有序的基础上修改
        分治合并(递归二分合并)
        将k个链表配对对同一个链表合并，然后再合并
        """
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, left, right):
        # 如果相同，就直接返回
        if left == right:
            return lists[left]
        # 越界了，左边界超过右边界
        if left > right:
            return
        # 二分
        # 递归合并左边，合并右边。然后再合并到一起
        mid = (left + right) / 2
        return self.merge_two_list(self.merge(lists, left, mid),
                                   self.merge(lists, mid + 1, right))

    def merge_two_list(self, a, b):
        # leetcode.21 合并两个链表
        dummy = tail = ListNode()
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        if b:
            tail.next = b
        if a:
            tail.next = a
        return dummy.next
