# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
#  请将其重新排列后变为：
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例 1：
#
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
#
#  示例 2：
#
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
#
#
#  提示：
#
#
#  链表的长度范围为 [1, 5 * 10⁴]
#  1 <= node.val <= 1000
#
#
#  Related Topics 栈 递归 链表 双指针 👍 1383 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        1.将链表平均分成两半，断开(slow.next = None)
        2.将第二个链表逆序
        3.依次连接两个链表(逆序节点塞到正序节点中）
        """
        if not head:
            return head
        # 找到中点--双指针
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 断开链表
        mid_head = slow.next
        slow.next = None
        # 反转链表
        cur = mid_head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 合并链表，逆序节点塞到正序节点中
        new_mid_head = pre
        while new_mid_head:
            tmp = new_mid_head.next
            new_mid_head.next = head.next
            head.next = new_mid_head
            head = new_mid_head.next
            new_mid_head = tmp

# leetcode submit region end(Prohibit modification and deletion)
