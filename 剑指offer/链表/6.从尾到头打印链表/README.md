# 题目

<p>输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>head = [1,3,2]
<strong>输出：</strong>[2,3,1]</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= 链表长度 &lt;= 10000</code></p>

# Python

```python
def reversePrint(self, head: ListNode) -> List[int]:
    result = list()
    if head is None:
        return result
    while head:
        result.append(head.val)
        head = head.next
    return result[::-1]
```

# Go

```go
/*
遍历一遍把val添加到数组中，然从后向前遍历数组并添加到结果列表中
*/
func reversePrint(head *ListNode) []int {
   stack := []int{}
   result := []int{}
   if head == nil {
      return result
   }
   for head != nil {
      stack = append(stack, head.Val)
      head = head.Next
   }

   for i := len(stack)-1; i >-1; i-- {
      result = append(result, stack[i])
   }
   return result
}
```
