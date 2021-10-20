# 题目
<p>给你链表的头结点 <code>head</code> ，请将其按 <strong>升序</strong> 排列并返回 <strong>排序后的链表</strong> 。</p>

<p><b>进阶：</b></p>

<ul>
	<li>你可以在 <code>O(n log n)</code> 时间复杂度和常数级空间复杂度下，对链表进行排序吗？</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg" style="width: 302px; "/>
<pre>
<b>输入：</b>head = [4,2,1,3]
<b>输出：</b>[1,2,3,4]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg" style="width: 402px; " />
<pre>
<b>输入：</b>head = [-1,5,3,4,0]
<b>输出：</b>[-1,0,3,4,5]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>head = []
<b>输出：</b>[]
</pre>

<p> </p>

<p><b>提示：</b></p>

<ul>
	<li>链表中节点的数目在范围 <code>[0, 5 * 10<sup>4</sup>]</code> 内</li>
	<li><code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code></li>
</ul>
<div><div>Related Topics</div><div><li>链表</li><li>双指针</li><li>分治</li><li>排序</li><li>归并排序</li></div></div>

# Python

```python
class Solution:
    """
    时间复杂度要求：nlogn 考虑二分法-归并排序
        归并排序分为：
        递归方式：
        先分割，然后归并时排序
            - 归并-leetcode.21题-合并两个有序链表
                - 遍历两个链表节点，比较值大小，小的加入链表，交替进行
            - 分割-leetcode.876题-找到链表中点
                - 找到中点进行拆分
                - 使用快慢指针，要找到第一个中值，指针初始不一致
    """

    def sortList(self, head: ListNode) -> ListNode:
        # 先分割
        # base case，head和head.next 存在才排序的必要
        if not head or not head.next:
            return head
        # 快慢指针
        # 初始化不一致，slow在偶数时找到第一个中值
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 从中间分割成2个链表
        mid = slow.next
        slow.next = None
        # 对链表进行排序
        return self.megre(self.sortList(head), self.sortList(mid))

    def megre(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            # 把l1交换成小值节点
            if l1.val > l2.val:
                l1, l2 = l2, l1
            # tail.next指向小值节点
            tail.next = l1
            # 前进一步
            l1 = l1.next
            tail = tail.next
        # tail接上剩下的节点
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
```

# Go

```go
/*
   nlogn时间要求 ->二分法，使用 归并排序
   归并排序 分为：分,和
   分:快慢指针,找到中间第一个节点,拆分
   和:对拆分后的链表进行从小达到的排序遍历
*/
func sortList(head *ListNode) *ListNode {
   // 分
   if head == nil || head.Next == nil {
      return head
   }
   // 快慢指针 不一致时 slow=中间第一个节点
   slow := head
   fast := head.Next
   for fast != nil && fast.Next != nil {
      slow = slow.Next
      fast = fast.Next.Next
   }
   // 取第一个中间节点的下一个做分开点
   mid := slow.Next
   slow.Next = nil
   // 对分开2个链表进行合并
   return merge(sortList(head), sortList(mid))
}
func merge(l1 *ListNode, l2 *ListNode) *ListNode {
   // dummy 辅助头节点
   dummy := &ListNode{}
   cur := dummy
   // 对l1和l2进行遍历 并用cur从小到大串联起来
   // 注意:链表每次循环的节点前进
   for l1 != nil && l2 != nil {
      if l1.Val > l2.Val {
         l1, l2 = l2, l1
      }
      cur.Next = l1
      l1 = l1.Next
      cur = cur.Next
   }
   // 连接上剩余节点
   if l1 != nil {
      cur.Next = l1
   }
   if l2 != nil {
      cur.Next = l2
   }
   return dummy.Next
}
```
