# 题目
<p>给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点<strong>被选的概率一样</strong>。</p>

<p><strong>进阶:</strong><br />
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？</p>

<p><strong>示例:</strong></p>

<pre>
// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();
</pre>

<div><div>Related Topics</div><div><li>水塘抽样</li><li>链表</li><li>数学</li><li>随机化</li></div></div>



# Python

```python
class Solution:
    """
    遍历一遍，抽取一个元素，保证每个节点获得的概率是一样的
    蓄水池算法
    每次只保留一个数，当遇到第 i 个数时，以 1/i的概率保留它，(i-1)/i的概率保留原来的数。
    """
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        res = 0
        cur = self.head
        while cur:
            count += 1
            rand = random.randint(1, count)
            if rand == count:
                res = cur.val
            cur = cur.next
        return res
```

# Go

```go
/** Returns a random node's value. */
func (this *Solution) GetRandom() int {
   count := 0
   res := 0
   cur := this.head
   for cur != nil {
      count += 1
      randNum := rand.Intn(count) + 1
      if randNum == count {
         res = cur.Val
      }
      cur = cur.Next
   }
   return res
}
```