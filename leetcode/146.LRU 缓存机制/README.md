# 题目
<div class="title__3Vvk">运用你所掌握的数据结构，设计和实现一个  <a href="https://baike.baidu.com/item/LRU" target="_blank">LRU (最近最少使用) 缓存机制</a> 。</div>

<div class="original__bRMd">
<div>
<p>实现 <code>LRUCache</code> 类：</p>

<ul>
	<li><code>LRUCache(int capacity)</code> 以正整数作为容量 <code>capacity</code> 初始化 LRU 缓存</li>
	<li><code>int get(int key)</code> 如果关键字 <code>key</code> 存在于缓存中，则返回关键字的值，否则返回 <code>-1</code> 。</li>
	<li><code>void put(int key, int value)</code> 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。</li>
</ul>

<p> </p>
</div>
</div>

<p><strong>进阶</strong>：你是否可以在 <code>O(1)</code> 时间复杂度内完成这两种操作？</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>输出</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>解释</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= capacity <= 3000</code></li>
	<li><code>0 <= key <= 10000</code></li>
	<li><code>0 <= value <= 10<sup>5</sup></code></li>
	<li>最多调用 <code>2 * 10<sup>5</sup></code> 次 <code>get</code> 和 <code>put</code></li>
</ul>
<div><div>Related Topics</div><div><li>设计</li><li>哈希表</li><li>链表</li><li>双向链表</li></div></div>

# Python

```python
class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头节点和尾节点
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果key存在，先通过哈希表找到位置，再移到头部
        node = self.cache[key]
        self.move2head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果key不存在，创建一个新的节点
            node = DLinkNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加到链表头部
            self.add2head(node)
            self.size += 1
            # 超出容量，删除链表尾部节点
            if self.size > self.capacity:
                remove = self.remove_tail()
                # 删除哈希表中对应的节点
                self.cache.pop(remove.key)
                self.size -= 1
        else:
            # 如果key存在，先通过哈希表定位，再修改value，最后移到头部
            node = self.cache[key]
            node.value = value
            self.move2head(node)

    # 添加节点到链表头部
    def add2head(self, node):
        # 节点接入链表头部
        node.pre = self.head
        node.next = self.head.next
        # 头部接入节点
        # 原头部节点的pre指向node
        # 头节点next指向node
        self.head.next.pre = node
        self.head.next = node

    # 删除节点
    def remove_node(self, node):
        # 跳过当前节点
        # 节点上个节点next = 节点下一个节点
        # 节点下一个节点pre = 节点上一个节点
        node.pre.next = node.next
        node.next.pre = node.pre

    # 移动节点到头部
    def move2head(self, node):
        # 删除当前节点，并添加当前节点到头部
        self.remove_node(node)
        self.add2head(node)

    # 删除尾部节点
    def remove_tail(self):
        # 取出尾节点，并删除
        node = self.tail.pre
        self.remove_node(node)
        return node
```

# Go

```go
package main

type DLinkNode struct {
   key, value int
   pre, next  *DLinkNode
}

func initDLinkNode(key, value int) *DLinkNode {
   return &DLinkNode{key: key, value: value}
}

type LRUCache struct {
   size       int
   capacity   int
   cache      map[int]*DLinkNode
   head, tail *DLinkNode
}

func Constructor(capacity int) LRUCache {
   l := LRUCache{
      cache:    map[int]*DLinkNode{},
      head:     initDLinkNode(0, 0),
      tail:     initDLinkNode(0, 0),
      capacity: capacity,
      size: 0,
   }
   l.head.next = l.tail
   l.tail.pre = l.head
   return l
}

func (this *LRUCache) Get(key int) int {
   /*
      不存在：返回-1，
      存在：先移动到头部，再返回
   */
   if _, ok := this.cache[key]; !ok {
      return -1
   }
   node := this.cache[key]
   this.move2Head(node)
   return node.value
}

func (this *LRUCache) Put(key int, value int) {
   /*
      不存在：初始化节点，存入哈希表，存入链表头部，大小+1，检查容量大小
         - 容量满：删除链表尾部节点，并在哈希表中删除，大小-1
      存在：从哈希表中取出node，更新value，并存入链表头部
   */
   if _, ok := this.cache[key]; !ok {
      node := initDLinkNode(key, value)
      this.cache[key] = node
      this.add2Head(node)
      this.size += 1
      if this.size > this.capacity {
         removed := this.removeTail()
         delete(this.cache, removed.key)
         this.size -= 1
      }

   } else {
      node := this.cache[key]
      node.value = value
      this.move2Head(node)
   }
}

func (this *LRUCache) add2Head(node *DLinkNode) {
   node.pre = this.head
   node.next = this.head.next
   this.head.next.pre = node
   this.head.next = node
}
func (this *LRUCache) removeNode(node *DLinkNode) {
   node.pre.next = node.next
   node.next.pre = node.pre
}

func (this *LRUCache) move2Head(node *DLinkNode) {
   this.removeNode(node)
   this.add2Head(node)
}

func (this *LRUCache) removeTail() *DLinkNode {
   node := this.tail.pre
   this.removeNode(node)
   return node
}
```