# 题目
<p>将两个升序链表合并为一个新的 <strong>升序</strong> 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 </p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
<pre>
<strong>输入：</strong>l1 = [1,2,4], l2 = [1,3,4]
<strong>输出：</strong>[1,1,2,3,4,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [], l2 = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>两个链表的节点数目范围是 <code>[0, 50]</code></li>
	<li><code>-100 <= Node.val <= 100</code></li>
	<li><code>l1</code> 和 <code>l2</code> 均按 <strong>非递减顺序</strong> 排列</li>
</ul>
<div><div>Related Topics</div><div><li>递归</li><li>链表</li></div></div>

# Python

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 穿针引线，初始化链表头和尾
    # 用尾节点去链接新的节点，谁小就链接上，同时新链表和对应链表进一步
    # 最后还有值的链表全部接到新链表后面
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l2:
        tail.next = l2
    if l1:
        tail.next = l1
    return dummy.next
```

# Go

```go
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
   dummy := &ListNode{0, nil}
   tail := dummy
   for l1 != nil && l2 != nil {
      if l1.Val <= l2.Val {
         tail.Next = l1
         l1 = l1.Next
      } else {
         tail.Next = l2
         l2 = l2.Next
      }
      tail = tail.Next
   }
   if l1 != nil {
      tail.Next = l1
   }
   if l2 != nil {
      tail.Next = l2
   }
   return dummy.Next
}
```