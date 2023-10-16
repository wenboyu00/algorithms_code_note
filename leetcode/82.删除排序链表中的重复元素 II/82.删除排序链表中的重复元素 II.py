# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
#  提示：
#
#
#  链表中节点数目在范围 [0, 300] 内
#  -100 <= Node.val <= 100
#  题目数据保证链表已经按升序 排列
#
#
#  Related Topics 链表 双指针 👍 1192 👎 0
from typing import Optional

from util.leetcode_type import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.next = None

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        current = pre.next
        while current:
            # 跳过当前重复节点, 让cur指向重复节点最后一个位置
            while current.next and current.val == current.next.val:
                current = current.next
            # 不管有没有重复 cur在每次循环都需要往下走
            current = current.next
            # pre和cur之间没有重复节点，pre后移
            if pre.next.next == current:
                pre = pre.next
            else:
                # pre直接跳过重复节点
                pre.next = current
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
