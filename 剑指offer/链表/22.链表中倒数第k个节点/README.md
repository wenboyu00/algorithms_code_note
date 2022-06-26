# 题目
<p>输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。</p>

<p>例如，一个链表有 <code>6</code> 个节点，从头节点开始，它们的值依次是 <code>1、2、3、4、5、6</code>。这个链表的倒数第 <code>3</code> 个节点是值为 <code>4</code> 的节点。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
给定一个链表: <strong>1->2->3->4->5</strong>, 和 <em>k </em><strong>= 2</strong>.

返回链表 4<strong>->5</strong>.</pre>

题目类似：leetcode.19。19题找到倒数k-1个节点后删除k节点

## Python

```python
def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    # fast 节点先前进 k
    # slow, fast同步前进，fast到队尾时 slow就是第k个节点
    fast,slow = head, head
    for i in range(k):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
```

## Go

```go
func getKthFromEnd(head *ListNode, k int) *ListNode {
   if head == nil {
      return head
   }
   fast := head
   slow := head
   for i := 0; i < k; i++ {
      fast = fast.Next
   }
   for fast != nil {
      fast = fast.Next
      slow = slow.Next
   }
   return slow
}
```
