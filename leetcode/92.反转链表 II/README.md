# 题目
给你单链表的头指针 <code>head</code> 和两个整数 <code>left</code> 和 <code>right</code> ，其中 <code>left <= right</code> 。请你反转从位置 <code>left</code> 到位置 <code>right</code> 的链表节点，返回 <strong>反转后的链表</strong> 。
<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], left = 2, right = 4
<strong>输出：</strong>[1,4,3,2,5]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>head = [5], left = 1, right = 1
<strong>输出：</strong>[5]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目为 <code>n</code></li>
	<li><code>1 <= n <= 500</code></li>
	<li><code>-500 <= Node.val <= 500</code></li>
	<li><code>1 <= left <= right <= n</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong> 你可以使用一趟扫描完成反转吗？</p>
<div><div>Related Topics</div><div><li>链表</li></div></div>

# Python

```python
class Solution:
    def __init__(self):
        self.successor = None

    # 反转以head为开始第left到right个节点，并返回头节点
    # 把反转一部分，分解为：前进到反转起点+反转起点后n个节点
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # base case
        if left == 1:
            # 反转起点后n个节点
            return self.reverseN(head, right)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    # 反转以 head 为起点的 n 个节点，返回新的头结点
    def reverseN(self, head: ListNode, n: int):
        # 记录第n + 1个节点，反转之后将head.next = successor
        if n == 1:
            self.successor = head.next
            return head
        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        # 让反转之后的 head 节点和后面的节点连起来
        head.next = self.successor
        return last
```

# Go

```go
// 声明全局遍历，successor为指向ListNode的地址的指针类型
var successor *ListNode

//反转以head为开始第left到right个节点，并返回头节点
func reverseBetween(head *ListNode, left int, right int) *ListNode {
   if left == 1 {
      return reverseN(head, left)
   }
   // 前进到反转的起点
   head.Next = reverseBetween(head.Next, left-1, right-1)
   return head
}

func reverseN(head *ListNode, n int) *ListNode {
   // 数量为1时保存head的后续，反转之后将head接上
   if n == 1 {
      successor = head.Next
      return head
   }
   last := reverseN(head.Next, n-1)
   head.Next.Next = head
   head.Next = successor
   return last
}
```