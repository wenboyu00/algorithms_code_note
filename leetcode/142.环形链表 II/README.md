# 题目
<p>给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 <code>null</code>。</p>

<p>为了表示给定链表中的环，我们使用整数 <code>pos</code> 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 <code>pos</code> 是 <code>-1</code>，则在该链表中没有环。<strong>注意，<code>pos</code> 仅仅是用于标识环的情况，并不会作为参数传递到函数中。</strong></p>

<p><strong>说明：</strong>不允许修改给定的链表。</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你是否可以使用 <code>O(1)</code> 空间解决此题？</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" style="height: 97px; width: 300px;" /></p>

<pre>
<strong>输入：</strong>head = [3,2,0,-4], pos = 1
<strong>输出：</strong>返回索引为 1 的链表节点
<strong>解释：</strong>链表中有一个环，其尾部连接到第二个节点。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 74px; width: 141px;" /></p>

<pre>
<strong>输入：</strong>head = [1,2], pos = 0
<strong>输出：</strong>返回索引为 0 的链表节点
<strong>解释：</strong>链表中有一个环，其尾部连接到第一个节点。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 45px; width: 45px;" /></p>

<pre>
<strong>输入：</strong>head = [1], pos = -1
<strong>输出：</strong>返回 null
<strong>解释：</strong>链表中没有环。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目范围在范围 <code>[0, 10<sup>4</sup>]</code> 内</li>
	<li><code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code></li>
	<li><code>pos</code> 的值为 <code>-1</code> 或者链表中的一个有效索引</li>
</ul>
<div><div>Related Topics</div><div><li>哈希表</li><li>链表</li><li>双指针</li></div></div>



# Python

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        meet_point = self.find_meet_point(head)
        if meet_point is None:
            return None

        fast = meet_point
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

    def find_meet_point(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow
            if fast == slow:
                return slow

        return None
```

# Go

```go
/*
1.找到双指针相遇点
2.某一个指针指向head，然后同步前进，直到相等时为相遇点
*/
func detectCycle(head *ListNode) *ListNode {
   if head == nil {
      return head
   }
   meetPoint := findMeetPoint(head)
   if meetPoint == nil {
      return nil
   }
   fast := meetPoint
   slow := head
   for fast != slow {
      fast = fast.Next
      slow = slow.Next
   }
   return slow
}

func findMeetPoint(head *ListNode) *ListNode {
   fast := head
   slow := head
   for fast != nil && fast.Next != nil {
      fast = fast.Next.Next
      slow = slow.Next
      if fast == slow {
         return slow
      }
   }
   return nil
}
```