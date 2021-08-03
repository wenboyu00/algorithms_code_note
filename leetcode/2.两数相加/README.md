# 题目
<p>给你两个 <strong>非空</strong> 的链表，表示两个非负的整数。它们每位数字都是按照 <strong>逆序</strong> 的方式存储的，并且每个节点只能存储 <strong>一位</strong> 数字。</p>

<p>请你将两个数相加，并以相同形式返回一个表示和的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数都不会以 0 开头。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>输出：</strong>[8,9,9,9,0,0,0,1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>每个链表中的节点数在范围 <code>[1, 100]</code> 内</li>
	<li><code>0 <= Node.val <= 9</code></li>
	<li>题目数据保证列表表示的数字不含前导零</li>
</ul>
<div><div>Related Topics</div><div><li>递归</li><li>链表</li><li>数学</li></div></div>

# Python

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化头节点和尾节点
        dummy = tail = ListNode(0)
        # 两数相加累计值
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # s%10，取尾数
            tail.next = ListNode(s % 10)
            tail = tail.next
            # s//10，取位数之外的数，在这里是进位数
            s = s // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
```

# Go

```go
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
   // l1和l2都为ListNode指针
   // 初始化头节点
   dummy := ListNode{Val: 0, Next: nil}
   // tail 等于头节点指针
   tail := &dummy
   s := 0
   // 在l1或者l2或者s不为空时继续循环
   for l1 != nil || l2 != nil || s > 0 {
      l1Val := 0
      l2Val := 0

      if l1 != nil {
         l1Val = l1.Val
      }
      if l2 != nil {
         l2Val = l2.Val
      }
      // s等于l1和l2和上次进位数的值
      s = l1Val + l2Val + s
      // s%10 取位数，s/10 取进位数
      node := ListNode{Val: s % 10, Next: nil}
      // Next等于新节点的地址
      tail.Next = &node
      fmt.Println(node)
      // 总和数 前进一位。l1，l2和尾节点都前进一位
      s = s / 10
      if l1 != nil {
         l1 = l1.Next
      }
      if l2 != nil {
         l2 = l2.Next
      }
      tail = tail.Next
   }
   // 因为头节点，值为空，next节点为第一个新节点地址，所以返回dummy.Next
   return dummy.Next
}
```