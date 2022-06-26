<p>给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。</p>

<p>返回删除后的链表的头节点。</p>

<p><strong>注意：</strong>此题对比原题有改动</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> head = [4,5,1,9], val = 5
<strong>输出:</strong> [4,1,9]
<strong>解释: </strong>给定你链表中值为&nbsp;5&nbsp;的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -&gt; 1 -&gt; 9.
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> head = [4,5,1,9], val = 1
<strong>输出:</strong> [4,5,9]
<strong>解释: </strong>给定你链表中值为&nbsp;1&nbsp;的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -&gt; 5 -&gt; 9.
</pre>

<p>&nbsp;</p>

<p><strong>说明：</strong></p>

<ul>
	<li>题目保证链表中节点的值互不相同</li>
	<li>若使用 C 或 C++ 语言，你不需要 <code>free</code> 或 <code>delete</code> 被删除的节点</li>
</ul>
# Python

```python
"""
dummy作为head前节点 方便返回内容
pre作为cur的前节点，方便删除cur的内容
"""

def deleteNode(self, head: ListNode, val: int) -> ListNode:
    dummy = ListNode(0, head)
    pre, cur = dummy, head
    while cur:
        if cur.val == val:
            pre.next = cur.next
        cur = cur.next
        pre = pre.next
    return dummy.next
```

# Go

```go
func deleteNode(head *ListNode, val int) *ListNode {
   dummy := &ListNode{0, head}
   pre := dummy
   cur := head
   for cur != nil {
      if cur.Val == val {
         pre.Next = cur.Next
      }
      pre = pre.Next
      cur = cur.Next
   }
   return dummy.Next
}
```
