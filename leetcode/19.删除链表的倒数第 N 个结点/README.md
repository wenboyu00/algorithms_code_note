# 题目
<p>给你一个链表，删除链表的倒数第 <code>n</code><em> </em>个结点，并且返回链表的头结点。</p>

<p><strong>进阶：</strong>你能尝试使用一趟扫描实现吗？</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], n = 2
<strong>输出：</strong>[1,2,3,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [1], n = 1
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2], n = 1
<strong>输出：</strong>[1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中结点的数目为 <code>sz</code></li>
	<li><code>1 <= sz <= 30</code></li>
	<li><code>0 <= Node.val <= 100</code></li>
	<li><code>1 <= n <= sz</code></li>
</ul>
<div><div>Related Topics</div><div><li>链表</li><li>双指针</li></div></div>

# Python

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if head is None:
        return head
    # dummy节点用来辅助删除头节点，slow=dummy 同理
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy.next
    # fast前进n步
    for i in range(n):
        fast = fast.next
    # fast到达尾部时，slow刚好是 n-1位置
    while fast:
        fast = fast.next
        slow = slow.next
    # slow.nex是n位置的节点，删除
    slow.next = slow.next.next

    return dummy.next
```

# Go

```go
    if head == nil {
      return head
   }
   dummy := &ListNode{0, head}
   slow := dummy
   fast := dummy.Next

   for i := 0; i < n; i++ {
      fast = fast.Next
   }

   for fast != nil {
      fast = fast.Next
      slow = slow.Next
   }
   slow.Next = slow.Next.Next

   return dummy.Next
}
```