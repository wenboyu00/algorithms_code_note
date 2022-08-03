# 题目
<p>给你一个链表数组，每个链表都已经按升序排列。</p>

<p>请你将所有链表合并到一个升序链表中，返回合并后的链表。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>lists = [[1,4,5],[1,3,4],[2,6]]
<strong>输出：</strong>[1,1,2,3,4,4,5,6]
<strong>解释：</strong>链表数组如下：
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
将它们合并到一个有序链表中得到。
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>lists = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>lists = [[]]
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10^4</code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10^4 &lt;= lists[i][j] &lt;= 10^4</code></li>
	<li><code>lists[i]</code> 按 <strong>升序</strong> 排列</li>
	<li><code>lists[i].length</code> 的总和不超过 <code>10^4</code></li>
</ul>
<div><div>Related Topics</div><div><li>链表</li><li>分治</li><li>堆（优先队列）</li><li>归并排序</li></div></div><br>

# Python

```python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    """
    在leetcode.21 合并两个有序的基础上修改
    分治合并(递归二分合并)
    将k个链表配对对同一个链表合并，然后再合并
    """
    return self.merge(lists, 0, len(lists) - 1)

def merge(self, lists, left, right):
    # 如果相同，就直接返回
    if left == right:
        return lists[left]
    # 越界了，左边界超过右边界
    if left > right:
        return
    # 二分
    # 递归合并左边，合并右边。然后再合并到一起
    mid = (left + right) / 2
    return self.merge_two_list(self.merge(lists, left, mid),
                               self.merge(lists, mid + 1, right))

def merge_two_list(self, a, b):
    # leetcode.21 合并两个链表
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if b:
        tail.next = b
    if a:
        tail.next = a
    return dummy.next
```

# Go

```go
func mergeKLists(lists []*ListNode) *ListNode {
   return merge(lists, 0, len(lists)-1)
}
func merge(lists []*ListNode, left int, right int) *ListNode {
   // base case 递归结束条件
   // - 相同数组
   if left == right {
      return lists[left]
   }
   // - 超过边界
   if left > right {
      return nil
   }
   // 二分后列表，进行递归合并
   mid := (left + right) / 2
   return mergeTwoList(merge(lists, left, mid), merge(lists, mid+1, right))
}

func mergeTwoList(a *ListNode, b *ListNode) *ListNode {
   // leetcode.21 穿针引线合并两个链表
   dummy := &ListNode{}
   tail := dummy
   for a != nil && b != nil {
      if a.Val <= b.Val {
         tail.Next = a
         a = a.Next
      } else {
         tail.Next = b
         b = b.Next
      }
      tail = tail.Next
   }
   if a != nil {
      tail.Next = a
   }
   if b != nil {
      tail.Next = b
   }
   return dummy.Next
}
```