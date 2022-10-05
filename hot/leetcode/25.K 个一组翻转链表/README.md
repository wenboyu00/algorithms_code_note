# 题目
<p>给你一个链表，每 <em>k </em>个节点一组进行翻转，请你返回翻转后的链表。</p>

<p><em>k </em>是一个正整数，它的值小于或等于链表的长度。</p>

<p>如果节点总数不是 <em>k </em>的整数倍，那么请将最后剩余的节点保持原有顺序。</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以设计一个只使用常数额外空间的算法来解决此问题吗？</li>
	<li><strong>你不能只是单纯的改变节点内部的值</strong>，而是需要实际进行节点交换。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], k = 2
<strong>输出：</strong>[2,1,4,3,5]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5], k = 3
<strong>输出：</strong>[3,2,1,4,5]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = [1,2,3,4,5], k = 1
<strong>输出：</strong>[1,2,3,4,5]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>head = [1], k = 1
<strong>输出：</strong>[1]
</pre>

<ul>
</ul>

<p><strong>提示：</strong></p>

<ul>
	<li>列表中节点的数量在范围 <code>sz</code> 内</li>
	<li><code>1 <= sz <= 5000</code></li>
	<li><code>0 <= Node.val <= 1000</code></li>
	<li><code>1 <= k <= sz</code></li>
</ul>
<div><div>Related Topics</div><div><li>递归</li><li>链表</li></div></div>

# Python

```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        k为一组反转链表
        递归反转k个节点
        1.定义a，b并赋值为head，b前进k个节点。反转a~b之间节点
        2.递归后续链表并连接起来
        """
        if head is None:
            return head
        # 区间[a,b)包含k个待反转
        a = b = head
        # b前进k个达到反转结束位置
        for i in range(k):
            # 不足k个，不需要反转 base case
            if b is None:
                return head
            b = b.next
        # 反转前k个元素
        new_head = self.reverseAB(a, b)
        # 递归反转后续链表并链接起来
        a.next = self.reverseKGroup(b, k)
        return new_head

    def reverseAB(self, a: ListNode, b: ListNode):
        # 反转区间[a,b)的元素，左闭右开
        pre, cur = None, a
        # cur = b 时终止，即a~(b-1)
        while cur != b:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp
        # 返回反转后头节点
        return pre
```

# Go

```go
func reverseKGroup(head *ListNode, k int) *ListNode {
   if head == nil {
      return head
   }
   a := head
   b := head
   // b节点前进k位，反转a~b之间共k个节点
   // 如果数量不够，就不反转直接返回
   for i := 0; i < k; i++ {
      if b == nil {
         return head
      }
      b = b.Next
   }
   // 反转ab，再对后续进行递归
   newHead := reverseAB(a, b)
   a.Next = reverseKGroup(b, k)
   return newHead
}

func reverseAB(a *ListNode, b *ListNode) *ListNode {
   // 反转a-(b-1)之间的节点，并返回新头节点
   var pre *ListNode
   cur := a
   // cur==b，完成a~b之间的反转
   for cur != b {
      // 实现反转
      tmp := cur.Next
      cur.Next = pre

      // 前，当前节点进一步
      pre = cur
      cur = tmp
   }
   return pre
}
```

