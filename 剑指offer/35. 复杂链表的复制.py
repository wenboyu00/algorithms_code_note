# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指
# 向链表中的任意节点或者 null。
#
#
#
#  示例 1：
#
#
#
#  输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
#  示例 2：
#
#
#
#  输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
#
#  示例 3：
#
#
#
#  输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
#
#  示例 4：
#
#  输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#
#
#
#
#  提示：
#
#
#  -10000 <= Node.val <= 10000
#  Node.random 为空（null）或指向链表中的节点。
#  节点数目不超过 1000 。
#
#
#
#
#  注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-point
# er/
#
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # 在原节点旁边插入复制节点
        cur = head
        while cur:
            new = Node(cur.val, cur.next, None)
            cur.next = new
            cur = new.next
        # 对插入的复制节点赋值random关系
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        # 解开节点为2个链表
        old = head
        new = head.next
        new_head = head.next
        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next else None
            old = old.next
            new = new.next

        return new_head
# leetcode submit region end(Prohibit modification and deletion)
