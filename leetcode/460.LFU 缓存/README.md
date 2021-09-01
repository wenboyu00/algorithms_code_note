# 题目
<p>请你为 <a href="https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95">最不经常使用（LFU）</a>缓存算法设计并实现数据结构。</p>

<p>实现 <code>LFUCache</code> 类：</p>

<ul>
	<li><code>LFUCache(int capacity)</code> - 用数据结构的容量 <code>capacity</code> 初始化对象</li>
	<li><code>int get(int key)</code> - 如果键存在于缓存中，则获取键的值，否则返回 -1。</li>
	<li><code>void put(int key, int value)</code> - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 <strong>最近最久未使用</strong> 的键。</li>
</ul>

<p><strong>注意</strong>「项的使用次数」就是自插入该项以来对其调用 <code>get</code> 和 <code>put</code> 函数的次数之和。使用次数会在对应项被移除后置为 0 。</p>

<p>为了确定最不常使用的键，可以为缓存中的每个键维护一个 <strong>使用计数器</strong> 。使用计数最小的键是最久未使用的键。</p>

<p>当一个键首次插入到缓存中时，它的使用计数器被设置为 <code>1</code> (由于 put 操作)。对缓存中的键执行 <code>get</code> 或 <code>put</code> 操作，使用计数器的值将会递增。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
<strong>输出：</strong>
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

<strong>解释：</strong>
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);   // cache=[1,_], cnt(1)=1
lFUCache.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lFUCache.get(1);      // 返回 1
                      // cache=[1,2], cnt(2)=1, cnt(1)=2
lFUCache.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                      // cache=[3,1], cnt(3)=1, cnt(1)=2
lFUCache.get(2);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
                      // cache=[3,1], cnt(3)=2, cnt(1)=2
lFUCache.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                      // cache=[4,3], cnt(4)=1, cnt(3)=2
lFUCache.get(1);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
                      // cache=[3,4], cnt(4)=1, cnt(3)=3
lFUCache.get(4);      // 返回 4
                      // cache=[3,4], cnt(4)=2, cnt(3)=3</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= capacity, key, value <= 10<sup>4</sup></code></li>
	<li>最多调用 <code>10<sup>5</sup></code> 次 <code>get</code> 和 <code>put</code> 方法</li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以为这两种操作设计时间复杂度为 <code>O(1)</code> 的实现吗？</p>
<div><div>Related Topics</div><div><li>设计</li><li>哈希表</li><li>链表</li><li>双向链表</li></div></div>

# Python

```python
class Node:
    """
    双向链表节点
    """

    def __init__(self, key=None, val=None, freq=0):
        self.key = key
        self.value = val
        self.pre = None
        self.next = None
        self.freq = freq


class DLinkedList:
    """
    双向链表和一些列所需要的操作
    """

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert_first(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def delete(self, node):
        if self.head.next == self.tail:
            return
        node.pre.next = node.next
        node.next.pre = node.pre

    def get_last(self):
        if self.head.next == self.tail:
            return None
        return self.tail.pre

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:
    def __init__(self, capacity: int):
        """
        key_map: {key: Node} - 字典
        freq_map: {freq: LinkedList} -字典
        """
        self.capacity = capacity
        self.min_freq = 0
        self.freq_map = dict()
        self.key_map = dict()

    def get(self, key: int) -> int:
        """
        获得元素
        - 如果存在 就返回应对val，更新访问元素访问频率
        - 如果不在，返回 -1
        """
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._increase(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        插入指定key:value
        如果key存在则更新value和频率
        如果key不存在，计划插入新元素
            - 如果已满，则删除频率最低的元素，
            - 插入新元素
        """
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._increase(node)
        else:
            if self.capacity == 0:
                return
            if len(self.key_map) == self.capacity:
                self._remove_min_freq_node()
            node = Node(key, value, 1)
            self._increase(node, True)
            self.key_map[key] = node

    def _increase(self, node, is_new_node=False):
        """
        更新节点访问频率(freq)
        """
        if is_new_node:
            self.min_freq = 1
            self._insert_first(node)
        else:
            self._delete(node)
            node.freq += 1
            self._insert_first(node)
            if self.min_freq not in self.freq_map:
                self.min_freq += 1

    def _insert_first(self, node):
        """
        根据节点的频率，插入对应的LinkedList中，没有则创建
        """
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DLinkedList()
        d_linked_list = self.freq_map[node.freq]
        d_linked_list.insert_first(node)

    def _delete(self, node):
        if node.freq not in self.freq_map:
            return
        d_linked_list = self.freq_map[node.freq]
        freq = node.freq
        d_linked_list.delete(node)
        # 列表为空时，删除freq_map上的索引
        if d_linked_list.is_empty():
            del self.freq_map[freq]
        return node.key

    def _remove_min_freq_node(self):
        """
        删除频率最低的元素
        找到freq_map[min_freq]中最后一个节点删除，同时在key_map也删除
        如果链表为空，则删除此链表
        """
        d_linked_list = self.freq_map[self.min_freq]
        node = d_linked_list.get_last()
        d_linked_list.delete(node)
        del self.key_map[node.key]
        # 列表为空时，删除freq_map上的索引
        if d_linked_list.is_empty():
            del self.freq_map[node.freq]
```

# Go

```go
type Node struct {
   key, value, freq int
   pre, next        *Node
}

type DLinkedList struct {
   head, tail *Node
}

func initDLinkedList() *DLinkedList {
   DLinked := &DLinkedList{
      head: &Node{key: 0, value: 0},
      tail: &Node{key: 0, value: 0},
   }
   DLinked.head.next = DLinked.tail
   DLinked.tail.pre = DLinked.head
   return DLinked
}
func (this *DLinkedList) addFirst(node *Node) {
   node.next = this.head.next
   node.pre = this.head
   this.head.next.pre = node
   this.head.next = node

}
func (this *DLinkedList) delete(node *Node) int {
   if this.head.next == this.tail {
      return -1
   }
   node.pre.next = node.next
   node.next.pre = node.pre
   node.next = nil
   node.pre = nil
   return node.key
}
func (this *DLinkedList) getLast() *Node {
   if this.head.next == this.tail {
      return nil
   }
   return this.tail.pre
}
func (this *DLinkedList) isEmpty() bool {
   return this.head.next == this.tail
}

type LFUCache struct {
   capacity int
   keyMap   map[int]*Node
   freqMap  map[int]*DLinkedList
   minFreq  int
}

func Constructor(capacity int) LFUCache {
   lfu := LFUCache{capacity: capacity,
      keyMap:  map[int]*Node{},
      freqMap: map[int]*DLinkedList{},
      minFreq: 0,
   }
   return lfu
}

func (this *LFUCache) Get(key int) int {
   // 获得值并更新freq值
   if node, ok := this.keyMap[key]; ok {
      // 更新freq值
      this.updateFreqMap(node, false)
      return node.value
   }
   return -1

}

func (this *LFUCache) Put(key int, value int) {
   if this.capacity == 0 {
      return
   }
   if _, ok := this.keyMap[key]; ok {
      node := this.keyMap[key]
      node.value = value
      this.updateFreqMap(node, false)
   } else {
      // 超过容量删除
      if len(this.keyMap) == this.capacity {
         this.removeMinFreqLastNode()
      }
      node := &Node{key: key, value: value, freq: 1}
      // 更新到keyMap
      this.keyMap[key] = node
      // 更新到FreqMap
      this.updateFreqMap(node, true)
   }

}

func (this *LFUCache) updateFreqMap(node *Node, isNew bool) {
   if isNew {
      this.minFreq = 1
      // 插入到链表头部
      this.insertFirst(node)
   } else {
      // 删除链表在原有位置
      this.deleteNode(node)
      // 频率+1
      node.freq += 1
      // 插入到链表头部
      this.insertFirst(node)
      // 更新最小freq
      if _, ok := this.freqMap[this.minFreq]; !ok {
         this.minFreq += 1
      }
   }
}

func (this *LFUCache) insertFirst(node *Node) {
   // 插入节点到对应freq对应的链表
   if _, ok := this.freqMap[node.freq]; !ok {
      this.freqMap[node.freq] = initDLinkedList()
   }

   dLinkedList := this.freqMap[node.freq]
   dLinkedList.addFirst(node)
}

func (this *LFUCache) deleteNode(node *Node) {
   // 在freq链表中删除节点
   if _, ok := this.freqMap[node.freq]; !ok {
      return
   }
   dLinkedList := this.freqMap[node.freq]
   dLinkedList.delete(node)
   // 此freq链表不存在就删除
   if dLinkedList.isEmpty() {
      delete(this.freqMap, node.freq)
   }
}
func (this *LFUCache) removeMinFreqLastNode() {
   // 在freq 链表找到最少频率的最后一个节点，并删除
   dLinkedList := this.freqMap[this.minFreq]
   node := dLinkedList.getLast()
   dLinkedList.delete(node)
   // 在keyMap删除节点
   delete(this.keyMap, node.key)
   // 此freq链表不存在就删除
   if dLinkedList.isEmpty() {
      delete(this.freqMap, this.minFreq)

   }
}
```