# 题目
<p>定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL
<strong>输出:</strong> 5-&gt;4-&gt;3-&gt;2-&gt;1-&gt;NULL</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= 节点个数 &lt;= 5000</code></p>

<p>&nbsp;</p>

<p><strong>注意</strong>：本题与主站 206 题相同：<a href="https://leetcode-cn.com/problems/reverse-linked-list/">https://leetcode-cn.com/problems/reverse-linked-list/</a></p>

# Python

```python
"""
递归
不进入递归中，只思考每次中的效果
递归结束条件：not cur and not cur.next
递归过程：
- 进入递归，把最后一个节点（当前的队尾，结果的队首）传递出去 last = self.reverse(cur.next)
- 当前节点下个的指向当前节点 cur.next.next = cur
- 取消之前指向 cur.next = None
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        return self.reverse(head)

    def reverse(self, cur):
        if not cur or not cur.next:
            return cur
        last = self.reverse(cur.next)
        cur.next.next = cur
        cur.next = None
        return last
```

# Go

```go
/*
迭代方式
pre 前节点，迭代结束后成为队尾节点
cur 当前节点
循环时：
    把cur.next保存到tmp
    把cur.next 只想pre，实现反转
    推进节点-注意推进顺序，先pre后cur：
        - pre = cur 前节点推荐到当前
        - cur = tmp 当前节点推进到原next节点

*/
func reverseList(head *ListNode) *ListNode {
   if head == nil {
      return head
   }
   var pre *ListNode
   cur := head
   for cur != nil {
      tmp := cur.Next
      cur.Next = pre
        pre = cur
        cur = tmp
   }
   return pre
}
```
