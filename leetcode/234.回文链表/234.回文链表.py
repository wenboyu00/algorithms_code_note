class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 快慢指针
        slow = fast = head
        # 用栈存储中间节点之前的节点
        stack = list()
        # 找到中间节点下一个节点，存储中间节点之前的值
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        # 处理奇偶问题
        # fast存在时，链表长度为奇数；slow要进一步，跳过中间点。
        if fast:
            slow = slow.next

        # 使用栈和中间节点后的数据对比，判断回文数
        while slow:
            val = stack.pop()
            if val != slow.val:
                return False
            slow = slow.next
        return True
