# 题目
<p>请实现 <code>copyRandomList</code> 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 <code>next</code> 指针指向下一个节点，还有一个 <code>random</code> 指针指向链表中的任意节点或者 <code>null</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png"></p>

<pre><strong>输入：</strong>head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>输出：</strong>[[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png"></p>

<pre><strong>输入：</strong>head = [[1,1],[2,1]]
<strong>输出：</strong>[[1,1],[2,1]]
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png"></strong></p>

<pre><strong>输入：</strong>head = [[3,null],[3,0],[3,null]]
<strong>输出：</strong>[[3,null],[3,0],[3,null]]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>head = []
<strong>输出：</strong>[]
<strong>解释：</strong>给定的链表为空（空指针），因此返回 null。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-10000 &lt;= Node.val &lt;= 10000</code></li>
	<li><code>Node.random</code>&nbsp;为空（null）或指向链表中的节点。</li>
	<li>节点数目不超过 1000 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 138 题相同：<a href="https://leetcode-cn.com/problems/copy-list-with-random-pointer/">https://leetcode-cn.com/problems/copy-list-with-random-pointer/</a></p>

<p>&nbsp;</p>

# Python

```python
"""
题目要求深拷贝
深拷贝 = 新建节点，关系一致
难点：新建时保持原有的节点关系
解决方法：哈希法，原节点映射拷贝节点 [原节点]  = [拷贝节点]
流程：
1. 拷贝节点，并建立原节点和拷贝节点关系
2. 根据原节点的关系，赋值拷贝节点的关系（next和random)
    a. 拷贝节点.next参考原节点.next指向的节点
    b. map.get(cur).next  是拷贝节点.next
    c. cur.next 是原节点.next指向的节点
    d. map.get(cur.next) 原节点.next节点映射的拷贝节点
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 原节点和拷贝节点映射表  [原节点] = 拷贝节点
        ori_copy_map = dict()
        cur = head
        # 拷贝节点值，并增加对应关系
        while cur:
            ori_copy_map[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        # 根据原节点的关系，赋值拷贝节点的关系
        while cur:
            # 拷贝节点的next = 原节点next 映射的拷贝节点
            ori_copy_map.get(cur).next = ori_copy_map.get(cur.next)
            # 拷贝节点的random = 原节点random 映射的拷贝节点
            ori_copy_map.get(cur).random = ori_copy_map.get(cur.random)
            cur = cur.next
        return ori_copy_map.get(head)
```

# Go

```go
/*
深复制 = 新建值，关系一致
1.拷贝值，构建原节点和新节点映射关系
2.拷贝关系，根据原节点关系 得到新节点关系
*/
func copyRandomList(head *Node) *Node {
   mapping := map[*Node]*Node{}
   // 1. 拷贝值
   cur := head
   for cur != nil {
      n := &Node{cur.Val, nil, nil}
      mapping[cur] = n
      cur = cur.Next
   }
   // 1. 拷贝关系
   cur = head
   for cur != nil{
      mapping[cur].Next = mapping[cur.Next]
      mapping[cur].Random = mapping[cur.Random]
      cur = cur.Next
   }
   return mapping[head]
}
```
