from typing import List

from util.leetcode_type import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result = list()
        if head is None:
            return result
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]

