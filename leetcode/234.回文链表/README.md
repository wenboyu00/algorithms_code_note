# 题目
<p>给你一个单链表的头节点 <code>head</code> ，请你判断该链表是否为回文链表。如果是，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
<pre>
<strong>输入：</strong>head = [1,2,2,1]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
<pre>
<strong>输入：</strong>head = [1,2]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点数目在范围<code>[1, 10<sup>5</sup>]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能否用&nbsp;<code>O(n)</code> 时间复杂度和 <code>O(1)</code> 空间复杂度解决此题？</p>
<div><div>Related Topics</div><div><li>栈</li><li>递归</li><li>链表</li><li>双指针</li></div></div>

# Python

```python
def isPalindrome(self, head: ListNode) -> bool:
    # 快慢指针
    slow = fast = head
    # 用栈存储中间节点之前的节点
    stack = list()
    # 找到中间节点下一个节点，存储中间节点之前的值
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    # 处理奇偶问题
    # fast存在时，链表长度为奇数；slow要进一步，跳过中间点。
    if fast:
        slow = slow.next

    # 使用栈和中间节点后的数据对比，判断回文数
    while slow:
        val = stack.pop()
        if val != slow.val:
            return False
        slow = slow.next
    return True
```

# Go

```go
func isPalindrome(head *ListNode) bool {
   slow := head
   fast := head
   stack := []int{}
   for fast != nil && fast.Next != nil {
      stack = append(stack, slow.Val)
      slow = slow.Next
      fast = fast.Next.Next
   }
   if fast != nil {
      slow = slow.Next
   }
   n := len(stack)
   for i := n - 1; i >= 0; i-- {
      val := stack[i]
      if val != slow.Val {
         return false
      }
      slow = slow.Next
   }
   return true
}
```